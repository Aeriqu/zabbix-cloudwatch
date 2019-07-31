#!/usr/bin/python
from basic_discovery import BasicDiscoverer


class Discoverer(BasicDiscoverer):
    def discovery(self, *args):
        response = self.client.list_distributions()

        data = list()
        for distribution in response['DistributionList']['Items']:
            distribution_data = {
                '{#CNAME}': distribution['AliasICPRecordals'][0]['CNAME'],
                '{#ID}': distribution['Id'],
            }
            data.append(distribution_data)

        return data
