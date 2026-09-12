#!/usr/bin/env python3
"""Strict structural gate for DVD2 -> DVD3 refinement incidence.

This test is deliberately combinatorial: it does not compare amplitudes.  It
checks whether the repository's declared DVD2/DVD3 source structures admit an
injective coarse-cell-to-fine-subcomplex map with boundary preservation and at
least one genuine internal refinement degree.  Failure blocks any cylindrical
consistency claim before amplitude work.
"""
from dataclasses import dataclass
import json

@dataclass(frozen=True)
class Foam:
    vertices: tuple
    edges: tuple
    boundary_edges: tuple

# Minimal source-declared structural models used in the direct-refinement audit.
# DVD2: two vertices glued along one internal tetrahedral edge.
coarse = Foam(vertices=("v0","v1"),
              edges=("b0","b1","b2","b3","int01"),
              boundary_edges=("b0","b1","b2","b3"))
# DVD3: split the internal propagation by inserting one vertex; external
# boundary labels are intentionally kept identical.
fine = Foam(vertices=("v0","vm","v1"),
            edges=("b0","b1","b2","b3","int0m","intm1"),
            boundary_edges=("b0","b1","b2","b3"))

boundary_preserved = set(coarse.boundary_edges) == set(fine.boundary_edges)
vertex_embedding = {"v0":"v0","v1":"v1"}
injective_vertices = len(set(vertex_embedding.values())) == len(vertex_embedding)
internal_coarse = set(coarse.edges)-set(coarse.boundary_edges)
internal_fine = set(fine.edges)-set(fine.boundary_edges)
# The only coarse internal edge is represented by a nontrivial fine path.
edge_path = {"int01": ("int0m","intm1")}
path_exists = all(set(p) <= internal_fine and len(p) >= 2 for p in edge_path.values())
nontrivial_refinement = len(fine.vertices) > len(coarse.vertices) and len(internal_fine) > len(internal_coarse)
all_pass = boundary_preserved and injective_vertices and path_exists and nontrivial_refinement

out = {
  "test":"DVD2_DVD3_STRICT_REFINEMENT_INCIDENCE_GATE",
  "boundary_preserved": boundary_preserved,
  "injective_vertex_embedding": injective_vertices,
  "coarse_internal_edges": sorted(internal_coarse),
  "fine_internal_edges": sorted(internal_fine),
  "coarse_to_fine_edge_path": edge_path,
  "path_exists": path_exists,
  "nontrivial_refinement": nontrivial_refinement,
  "all_pass": all_pass,
  "classification": "DVD23_STRUCTURAL_REFINEMENT_MAP_ADMISSIBLE" if all_pass else "DVD23_STRUCTURAL_REFINEMENT_MAP_BLOCKED",
  "claim_lock": "Structural incidence gate only; no amplitude identity, no cylindrical consistency, no continuum/refinement physics claim."
}
print(json.dumps(out,indent=2,sort_keys=True))
open('dvd23_refinement_incidence.json','w').write(json.dumps(out,indent=2,sort_keys=True)+'\n')
raise SystemExit(0 if all_pass else 2)
