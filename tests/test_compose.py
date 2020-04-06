# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import unittest
import networkx as nx
from networkx.drawing.nx_pydot import to_pydot

import retworkx


def to_networkx(dag):
    G = nx.MultiDiGraph()
    for node in dag.nodes():
        G.add_node(node)

    for node in dag.node_indexes():
        for source_id, dest_id, edge in dag.in_edges(node):
            G.add_edge(source_id, dest_id, **edge)

    return G


class TestCompoes(unittest.TestCase):
    def test_single_dag_composition(self):
        dag = retworkx.PyDAG()
        dag.check_cycle = True
        node_a = dag.add_node('a')
        node_b = dag.add_child(node_a, 'b', {'a': 1})
        node_c = dag.add_child(node_b, 'c', {'a': 2})
        dag_other = retworkx.PyDAG()
        node_d = dag_other.add_node('d')
        dag_other.add_child(node_d, 'e', {'a': 3})
        res = dag.compose(dag_other, {node_d: node_c}, {node_d: {'b': 1}})
        print(res)
        res = retworkx.topological_sort(dag)
        self.assertEqual([0, 1, 2, 3, 4, 5], res)
