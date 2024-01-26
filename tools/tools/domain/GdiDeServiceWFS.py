import json
from ..api.models.Common import KeyDollarListDict
from ..api.models.SettingsWFS import SettingsWFS

import logging

log = logging.getLogger()

class GdiDeServiceWFS(SettingsWFS):
    def __init__(self,
                 workspace,
                 config,
                 keywords=[],
                 srs = [],
                 fees = "",
                 accessConstraints = "",
                 internationalAbstract = "",
                 internationalTitle = "",
                 overrideMetadataEntries = {},
                 identifier = ""
                 ) -> None:
        super().__init__(workspace)
        self.wfs = json.loads(config["full_content"])
        self.metadata_entries = KeyDollarListDict(json.loads(config["metadata_entries"]))
        self.metadata_entries.update(overrideMetadataEntries)
        self.wfs["workspace"]["name"] = workspace
        self.wfs["keywords"]["string"] = list(set(keywords + json.loads(config["keywords"])))
        self.wfs["srs"]["string"] = srs if srs != [] else json.loads(config["srs"])
        self.wfs["fees"] = fees
        self.wfs["accessConstraints"] = accessConstraints
        self.wfs["internationalAbstract"]["de-DE"] = internationalAbstract
        self.wfs["internationalTitle"]["de-DE"] = internationalTitle
        self.wfs["getFeatureOutputTypes"]["string"] = json.loads(config["allowedOutputFormats"])
        self.wfs["metadata"]["entry"] = self.metadata_entries.serialize()
        self.wfs["identifiers"]["Identifier"][0]["identifier"] = identifier

        
    def put_payload(self):
        payload = { "wfs": self.wfs }
        with open("/tmp/payload_wfs.json", "w") as f:
            f.write(json.dumps(payload))
        return payload
        
        