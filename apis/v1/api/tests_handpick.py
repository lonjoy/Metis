# -*- coding: utf-8 -*-

from apis.models.test import Test

from . import Resource


class TestsHandpick(Resource):

    async def get(self, request):
        tests = (Test.objects(status=Test.STATUS_PUBLISHED, is_digest=True)
                 .order_by('-participate_number')
                 .skip(0).limit(10))
        return tests, 200
