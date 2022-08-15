import random

def generate_mock_string():
    return random.choice([ "foo", "bar", "baz", "qux", "fred", "plugh", "spam", "ham", "eggs" ])

def generate_mock_patient():
    return {
        "name": {
            "value": generate_mock_string(),
            "defining_code": {
                "terminology_id": {
                    "value": generate_mock_string(),
                    "_type": "TERMINOLOGY_ID"
                },
                "code_string": generate_mock_string(),
                "_type": "CODE_PHRASE"
            },
            "_type": "DV_CODED_TEXT"
        },
        "archetype_node_id": "at0000_1",
        "identities": [
            {
                "name": {
                    "value": generate_mock_string(),
                    "defining_code": {
                        "terminology_id": {
                            "value": generate_mock_string(),
                            "_type": "TERMINOLOGY_ID"
                        },
                        "code_string": generate_mock_string(),
                        "_type": "CODE_PHRASE"
                    },
                    "_type": "DV_CODED_TEXT"
                },
                "archetype_node_id": "at0000_1",
                "details": {
                    "name": {
                        "value": generate_mock_string(),
                        "defining_code": {
                            "terminology_id": {
                                "value": generate_mock_string(),
                                "_type": "TERMINOLOGY_ID"
                            },
                            "code_string": generate_mock_string(),
                            "_type": "CODE_PHRASE"
                        },
                        "_type": "DV_CODED_TEXT"
                    },
                    "archetype_node_id": "at0001",
                    "items": [
                        {
                            "name": {
                                "value": generate_mock_string(),
                                "defining_code": {
                                    "terminology_id": {
                                        "value": generate_mock_string(),
                                        "_type": "TERMINOLOGY_ID"
                                    },
                                    "code_string": generate_mock_string(),
                                    "_type": "CODE_PHRASE"
                                },
                                "_type": "DV_CODED_TEXT"
                            },
                            "archetype_node_id": "at0003",
                            "items": [
                                {
                                    "name": {
                                        "value": generate_mock_string(),
                                        "defining_code": {
                                            "terminology_id": {
                                                "value": generate_mock_string(),
                                                "_type": "TERMINOLOGY_ID"
                                            },
                                            "code_string": generate_mock_string(),
                                            "_type": "CODE_PHRASE"
                                        },
                                        "_type": "DV_CODED_TEXT"
                                    },
                                    "archetype_node_id": "at0012",
                                    "_type": "ELEMENT"
                                },
                                {
                                    "name": {
                                        "value": generate_mock_string(),
                                        "defining_code": {
                                            "terminology_id": {
                                                "value": generate_mock_string(),
                                                "_type": "TERMINOLOGY_ID"
                                            },
                                            "code_string": generate_mock_string(),
                                            "_type": "CODE_PHRASE"
                                        },
                                        "_type": "DV_CODED_TEXT"
                                    },
                                    "archetype_node_id": "at0013",
                                    "_type": "ELEMENT"
                                }
                            ],
                            "_type": "CLUSTER"
                        },
                        {
                            "name": {
                                "value": generate_mock_string(),
                                "defining_code": {
                                    "terminology_id": {
                                        "value": generate_mock_string(),
                                        "_type": "TERMINOLOGY_ID"
                                    },
                                    "code_string": generate_mock_string(),
                                    "_type": "CODE_PHRASE"
                                },
                                "_type": "DV_CODED_TEXT"
                            },
                            "archetype_node_id": "at0006",
                            "items": [
                                {
                                    "name": {
                                        "value": generate_mock_string(),
                                        "defining_code": {
                                            "terminology_id": {
                                                "value": generate_mock_string(),
                                                "_type": "TERMINOLOGY_ID"
                                            },
                                            "code_string": generate_mock_string(),
                                            "_type": "CODE_PHRASE"
                                        },
                                        "_type": "DV_CODED_TEXT"
                                    },
                                    "archetype_node_id": "at0018",
                                    "_type": "ELEMENT"
                                },
                                {
                                    "name": {
                                        "value": generate_mock_string(),
                                        "defining_code": {
                                            "terminology_id": {
                                                "value": generate_mock_string(),
                                                "_type": "TERMINOLOGY_ID"
                                            },
                                            "code_string": generate_mock_string(),
                                            "_type": "CODE_PHRASE"
                                        },
                                        "_type": "DV_CODED_TEXT"
                                    },
                                    "archetype_node_id": "at0019",
                                    "_type": "ELEMENT"
                                }
                            ],
                            "_type": "CLUSTER"
                        },
                        {
                            "name": {
                                "value": generate_mock_string(),
                                "defining_code": {
                                    "terminology_id": {
                                        "value": generate_mock_string(),
                                        "_type": "TERMINOLOGY_ID"
                                    },
                                    "code_string": generate_mock_string(),
                                    "_type": "CODE_PHRASE"
                                },
                                "_type": "DV_CODED_TEXT"
                            },
                            "archetype_node_id": "at0008",
                            "_type": "ELEMENT"
                        }
                    ],
                    "_type": "ITEM_TREE"
                },
                "_type": "PARTY_IDENTITY"
            }
        ],
        "_type": "PERSON"
    }