from django.test import TestCase

import pytest

class TestPricing:

    # Create a Pricing object with all required fields and save it to the database.
    def test_create_pricing_with_required_fields(self):
        pricing = Pricing(price=10, pricing_model='monthly', company=Company.objects.create(name='Test Company'))
        pricing.save()
        assert Pricing.objects.count() == 1

    # Create a Pricing object with all fields and set has_free_plan, has_free_trial, and is_open_source to True.
    def test_create_pricing_with_all_fields_and_true_flags(self):
        pricing = Pricing(price=10, pricing_model='monthly', has_free_plan=True, has_free_trial=True, is_open_source=True, company=Company.objects.create(name='Test Company'))
        pricing.save()
        assert Pricing.objects.count() == 1

    # Create a Pricing object with price set to 0 and has_free_plan set to False.
    def test_create_pricing_with_zero_price_and_false_free_plan(self):
        pricing = Pricing(price=0, pricing_model='monthly', has_free_plan=False, company=Company.objects.create(name='Test Company'))
        pricing.save()
        assert Pricing.objects.count() == 1

    # Create a Pricing object with pricing_model set to an invalid value.
    def test_create_pricing_with_invalid_pricing_model(self):
        with pytest.raises(ValueError):
            pricing = Pricing(price=10, pricing_model='invalid', company=Company.objects.create(name='Test Company'))
            pricing.save()

    # Create a Pricing object with has_free_plan and has_free_trial set to True, and pricing_model set to 'one time'.
    def test_create_pricing_with_true_free_plan_and_trial_and_one_time_pricing_model(self):
        pricing = Pricing(price=10, pricing_model='one time', has_free_plan=True, has_free_trial=True, company=Company.objects.create(name='Test Company'))
        pricing.save()
        assert Pricing.objects.count() == 1

    # Create a Pricing object with is_open_source set to True, and pricing_model set to 'yearly'.
    def test_create_pricing_with_true_open_source_and_yearly_pricing_model(self):
        pricing = Pricing(price=10, pricing_model='yearly', is_open_source=True, company=Company.objects.create(name='Test Company'))
        pricing.save()
        assert Pricing.objects.count() == 1
