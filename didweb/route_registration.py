from profile import Profile

from aries_cloudagent.protocols.coordinate_mediation.v1_0.route_manager import (
    RouteManager,
)
from aries_cloudagent.protocols.routing.v1_0.models.route_record import RouteRecord
from aries_cloudagent.wallet.base import BaseWallet


class RouteRegistrar:
    """No route ? No worries."""

    def __init__(
        self, profile: Profile, wallet: BaseWallet, routing_manager: RouteManager
    ):
        self.__profile = profile
        self.__wallet = wallet
        self.__routing_manager = routing_manager

    async def register_route(self, did: str) -> RouteRecord:
        """
        Register a route given a did and a recipient wallet
        :param did: DID on the receiving end of the route
        :param wallet_id: wallet on the receiving end of the route
        :return:
        """
        did_record = await self.__wallet.get_local_did(did)
        return await self.__routing_manager.route_public_did(
            profile=self.__profile, verkey=did_record.verkey
        )
