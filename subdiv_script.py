#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pycountry import pycountry
import json


class SubdivisionFixtures(object):
  """
  Horrible hacky script to extract subdivisions from the somewhat erroneous ISO-3166-2
  """
  INCLUDE_COUNTRIES = (
      (u'BR', 28),  # (ISO-3166 alpha2 code, kvasir.backend.models.country.pk)
      (u'IN', 84),
      (u'MX', 122),
  )

  EXCLUDE_SUBDIVISIONS = (
      u'BR-FN' # Fernando de Noronha
  )

  NAME_SUBSTITUTIONS = {
      u'BR-DF': u'Federal District',
      u'MX-DIF': u'Mexico City',
      u'IN-OR': u'Odisha',
  }

  NEW_SUBDIVISIONS = (
    {
      "alternative_names": [],
      "country": "IN",
      "iso_code": "IN-TG",
      "name": "Telangana",
      "type": "State"
    }
  )

  def handle(self):
    for country_iso_code, numerical_code in self.INCLUDE_COUNTRIES:
      country_name = pycountry.countries.get(alpha2=country_iso_code).name
      print '## ' + country_name + ' (' + country_iso_code + ')'


#   def _create_subdivision_types(self):
#     types = (x.type.capitalize() for x in pycountry.subdivisions)
#     return list(set(types))  # unique

#   def create_subdivisions(self):
#     subdivisions = []
#     subdivision_alternative_names = []
#     subdivision_types = []

#     all_subdivisions = (x for x in pycountry.subdivisions if any(u'%s-' % c[0] in x.code for c in self.INCLUDE_COUNTRIES))


if __name__ == '__main__':
  print "Running script ..."
  s = SubdivisionFixtures()
  s.handle()