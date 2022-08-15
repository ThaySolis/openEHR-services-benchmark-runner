from prov.model import ProvDocument

MOCK_VERSIONS = [
    {
        "id": "{PERSON_ID}::{SYSTEM_ID}::1",
        "committer": "{USER}",
        "contribution_id": "{CONTRIBUTION1_ID}"
    },
    {
        "id": "{PERSON_ID}::{SYSTEM_ID}::2",
        "committer": "{USER}",
        "contribution_id": "{CONTRIBUTION2_ID}"
    },
]

def create_mock_prov_document() -> ProvDocument:
    # creates the provenance document
    doc = ProvDocument()

    # PROV uses namespaces like XML.
    # All used namespaces must be declared explicitly, except the standard ones.
    doc.add_namespace("openehr", "http://schemas.openehr.org/v2")

    agents = set()
    version_ids = [ x["id"] for x in MOCK_VERSIONS ]
    for i in range(0, len(version_ids)):
        version_id = version_ids[i]

        version = [ x for x in MOCK_VERSIONS if x["id"] == version_id ][0]
        contribution_id = version["contribution_id"]
        committer_name_or_id = version["committer"]

        doc.entity(f"openehr:{version_id}", other_attributes = {"prov:type": "openehr:EHR_STATUS"})
        doc.activity(f"openehr:{contribution_id}", other_attributes = {"prov:type": "openehr:CONTRIBUTION"})
        doc.wasGeneratedBy(entity = f"openehr:{version_id}", activity = f"openehr:{contribution_id}")

        if committer_name_or_id is not None:
            if committer_name_or_id not in agents:
                agents.add(committer_name_or_id)
                doc.agent(f"openehr:committer_{committer_name_or_id}", other_attributes = {"prov:type": "openehr:PARTY_IDENTIFIED"})

            doc.wasAttributedTo(entity = f"openehr:{version_id}", agent = f"openehr:committer_{committer_name_or_id}")
            doc.wasAssociatedWith(activity = f"openehr:{contribution_id}", agent = f"openehr:committer_{committer_name_or_id}")

        if i > 0:
            previous_version_id = version_ids[i - 1]
            doc.wasDerivedFrom(f"openehr:{version_id}", f"openehr:{previous_version_id}")
            doc.used(f"openehr:{contribution_id}", f"openehr:{previous_version_id}")

    return doc

doc = create_mock_prov_document()
doc.plot(filename="TESTE.svg")
