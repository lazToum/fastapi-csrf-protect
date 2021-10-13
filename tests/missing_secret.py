#!/usr/bin/env python3
# Copyright (C) 2019-2020 All rights reserved.
# FILENAME:  missing_secret.py
# VERSION: 	 0.2.0
# CREATED: 	 2021-08-18 23:58
# AUTHOR: 	 Aekasitt Guruvanich <aekazitt@gmail.com>
# DESCRIPTION:
#
# HISTORY:
#*************************************************************
### Third-Party Packages ###
from fastapi.testclient import TestClient
from pytest import raises
### Local Modules ###
from . import *
from fastapi_csrf_protect import CsrfProtect

def validate_missing_secret_key(client: TestClient):
  with raises(RuntimeError) as err:
    @CsrfProtect.load_config
    def load_secret_key():
      return [('secret_key', None)]
    client.get('/protected')
  assert err.match('A secret key is required to use CSRF.')

def test_missing_secret_key_in_cookies(setup_cookies):
  validate_missing_secret_key(setup_cookies)

def test_missing_secret_key_in_headers(setup_context):
  validate_missing_secret_key(setup_context)