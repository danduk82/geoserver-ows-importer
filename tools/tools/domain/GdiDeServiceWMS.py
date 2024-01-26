import json
from ..api.models.Common import KeyDollarListDict
from ..api.models.SettingsWMS import SettingsWMS

import logging

log = logging.getLogger()

class GdiDeServiceWMS(SettingsWMS):
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
        self.wms = json.loads(config["full_content"])
        self.metadata_entries = KeyDollarListDict(json.loads(config["metadata_entries"]))
        self.metadata_entries.update(overrideMetadataEntries)
        self.wms["workspace"]["name"] = workspace
        self.wms["keywords"]["string"] = list(set(keywords + json.loads(config["keywords"])))
        self.wms["srs"]["string"] = srs if srs != [] else json.loads(config["srs"])
        self.wms["fees"] = fees
        self.wms["accessConstraints"] = accessConstraints
        self.wms["internationalAbstract"]["de-DE"] = internationalAbstract
        self.wms["internationalTitle"]["de-DE"] = internationalTitle
        self.wms["getMapMimeTypes"]["string"] = json.loads(config["getMapMimeTypes"])
        self.wms["metadata"]["entry"] = self.metadata_entries.serialize()
        self.wms["identifiers"]["Identifier"][0]["identifier"] = identifier

        
    def put_payload(self):
        payload = { "wms": self.wms }
        # with open("/tmp/payload_wms.json", "w") as f:
        #     f.write(json.dumps(payload))
        return payload
        
        