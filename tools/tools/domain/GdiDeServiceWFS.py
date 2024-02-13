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
        try:
            for to_remove in config["keywordsToRemove"].split(","):
                self.wfs["keywords"]["string"].remove(to_remove)
        except ValueError:
            log.debug("No keywords to remove found")
        try:
            self.wfs["srs"]["string"] = srs if srs != [] else json.loads(config["srs"])
        except KeyError:
            log.warning("No srs found in config")
        self.wfs["fees"] = fees
        self.wfs["accessConstraints"] = accessConstraints
        self.wfs["internationalAbstract"]["de-DE"] = internationalAbstract
        self.wfs["internationalTitle"]["de-DE"] = internationalTitle
        self.wfs["getFeatureOutputTypes"]["string"] = json.loads(config["allowedOutputFormats"])
        log.debug(f"identifier: {identifier}")
        self.metadata_entries.update({"inspire.spatialDatasetIdentifier": f"GDI-DE,https://www.gdi-de.org,{identifier}"})
        self.wfs["metadata"]["entry"] = self.metadata_entries.serialize()

        
    def put_payload(self):
        payload = { "wfs": self.wfs }
        # with open("/tmp/payload_wfs.json", "w") as f:
        #     f.write(json.dumps(payload))
        return payload
        
        