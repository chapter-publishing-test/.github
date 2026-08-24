from __future__ import annotations
import hashlib
import json
import re
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

class Suite(unittest.TestCase):
 def test_suite_manifest_is_bounded(self):
  data=json.loads((ROOT/'fixtures/suite.json').read_text()); self.assertEqual(data['repository'],'.github'); self.assertTrue(data['syntheticOnly']); self.assertGreaterEqual(len(data['assertions']),3)
 def test_fixture_digest_is_stable(self): self.assertEqual(hashlib.sha256((ROOT/'fixtures/suite.json').read_bytes()).hexdigest(),(ROOT/'fixtures/suite.sha256').read_text().strip())

if __name__=='__main__': unittest.main()
