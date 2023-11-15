import json
from ..api.models.Common import KeyDollarListDict
from ..api.models.SettingsWMS import SettingsWMS

import logging

log = logging.getLogger()

class GdiDeServiceWMS(SettingsWMS):
    def __init__(self,
                 workspace,
                 config,
                 name = "",
                 keywords=[],
                 srs = [],
                 fees = "",
                 accessConstraints = "",
                 internationalAbstract = "",
                 internationalTitle = "",
                 replacementMetadataEntries = {},
                 authorityUrl = "",
                 identifier = "",
                 onlineResource = "",
                 ) -> None:
        super().__init__(workspace)
        self.wms = json.loads(config["full_content"])
        self.metadata_entries = KeyDollarListDict(config["metadata_entries"])
        self.metadata_entries.update(replacementMetadataEntries)
        self.wms["workspace"]["name"] = workspace
        self.wms["name"] = name
        self.wms["keywords"]["string"] = keywords
        self.wms["srs"]["string"] = srs
        self.wms["fees"] = fees
        self.wms["accessConstraints"] = accessConstraints
        self.wms["internationalAbstract"]["de-DE"] = internationalAbstract
        self.wms["internationalTitle"]["de-DE"] = internationalTitle
        self.wms["getMapMimeTypes"]["string"] = config["getMapMimeTypes"]
        self.wms["metadata"]["entry"] = self.metadata_entries.serialize()
        self.wms["authorityURL"]["href"] = authorityUrl
        self.wms["Identifier"]["identifier"] = identifier
        self.wms["onlineResource"] = onlineResource

        
    def put_payload(self):
        payload = { "wms": self.wms }
        
        