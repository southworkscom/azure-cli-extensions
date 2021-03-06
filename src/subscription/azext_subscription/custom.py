# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_subscription.subscription.models import SubscriptionDefinition


def cli_subscription_create_subscription_definition(client, subscription_definition_name,
                                                    offer_type, subscription_display_name=None):
    if subscription_display_name is None:
        subscription_display_name = subscription_definition_name

    new_def = SubscriptionDefinition(
        subscription_display_name=subscription_display_name,
        offer_type=offer_type)

    return client.create(subscription_definition_name, new_def)
