#!/usr/bin/env python3
# Copyright (C) 2019-2020 All rights reserved.
# FILENAME:  missing_token.py
# VERSION: 	 0.2.0
# CREATED: 	 2020-11-26 16:14
# AUTHOR: 	 Aekasitt Guruvanich <aekazitt@gmail.com>
# DESCRIPTION:
#
# HISTORY:
#*************************************************************
### Third-Party Packages ###
from fastapi.testclient import TestClient
### Local Packages ###
from . import *
from fastapi_csrf_protect import CsrfProtect

def validate_missing_token_request(client: TestClient, route: str = '/protected'):
  ### Loads Config ###
  @CsrfProtect.load_config
  def get_secret_key():
    return [('secret_key', 'secret')]

  ### Get ###
  response           = client.get(route)

  ### Assertions ###
  assert response.status_code == 400
  assert response.json() == {'detail': 'Missing Cookie fastapi-csrf-token'}

def test_missing_token_request_in_cookies(setup_cookies):
  validate_missing_token_request(setup_cookies)

def test_missing_token_request_in_context(setup_context):
  validate_missing_token_request(setup_context)
