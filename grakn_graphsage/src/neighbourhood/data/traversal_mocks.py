import grakn_graphsage.src.neighbourhood.data.concept as concept
import grakn_graphsage.src.neighbourhood.data.traversal as trv
import grakn_graphsage.src.neighbourhood.data.executor as ex


def gen(elements):
    for el in elements:
        yield el


def mock_traversal_output():
    c = trv.ConceptInfoWithNeighbourhood(
        concept.ConceptInfo("0", "person", "entity"),
        gen([
            trv.NeighbourRole("employee", ex.TARGET_PLAYS, trv.ConceptInfoWithNeighbourhood(
                concept.ConceptInfo("1", "employment", "relationship"),
                gen([
                    trv.NeighbourRole("employer", ex.NEIGHBOUR_PLAYS, trv.ConceptInfoWithNeighbourhood(
                        concept.ConceptInfo("2", "company", "entity"), gen([])
                    )),
                    trv.NeighbourRole("employer", ex.NEIGHBOUR_PLAYS, trv.ConceptInfoWithNeighbourhood(
                        concept.ConceptInfo("2", "company", "entity"), gen([])
                    )),
                    trv.NeighbourRole("employer", ex.NEIGHBOUR_PLAYS, trv.ConceptInfoWithNeighbourhood(
                        concept.ConceptInfo("2", "company", "entity"), gen([])
                    ))
                ])
            )),
            trv.NeighbourRole("@has-name-owner", ex.TARGET_PLAYS, trv.ConceptInfoWithNeighbourhood(
                concept.ConceptInfo("3", "@has-name", "relationship"),
                gen([
                    trv.NeighbourRole("@has-name-value", ex.NEIGHBOUR_PLAYS, trv.ConceptInfoWithNeighbourhood(
                        concept.ConceptInfo("4", "name", "attribute", data_type='string', value="Employee Name"),
                        gen([])
                    )),
                    trv.NeighbourRole("@has-name-value", ex.NEIGHBOUR_PLAYS, trv.ConceptInfoWithNeighbourhood(
                        concept.ConceptInfo("4", "name", "attribute", data_type='string', value="Employee Name"),
                        gen([])
                    )),
                    trv.NeighbourRole("@has-name-value", ex.NEIGHBOUR_PLAYS, trv.ConceptInfoWithNeighbourhood(
                        concept.ConceptInfo("4", "name", "attribute", data_type='string', value="Employee Name"),
                        gen([])
                    ))
                ])
            ))

        ]))
    return c
