from .models import *
from django.shortcuts import HttpResponse


class Service(object):
    @staticmethod
    def get_GM_data(id):
        all_members = RGM.objects.all()
        Parent = GM.objects.get(id=id)
        total_members = len(all_members) + 1
        total_sales = Parent.sales
        commission = Parent.commission

        for rgm in all_members:
            total_sales += rgm.sales
            commission += rgm.commission
            print(commission)
        data = {'Parent': Parent, 'Child': all_members, 'commission': commission,
                'total_member': total_members, 'total_sales': total_sales, 'type': 'RGM'}
        return data

    @staticmethod
    def get_RGM_data(id):
        Parent = RGM.objects.get(id=id)
        all_members = AGM.objects.filter(RGM_id=Parent)
        total_members = len(all_members) + 1
        total_sales = Parent.sales
        commission = Parent.commission
        for agm in all_members:
            total_sales += agm.sales
            commission += agm.commission
        data = {'Parent': Parent, 'Child': all_members, 'commission': commission,
                'total_member': total_members, 'total_sales': total_sales, 'type': 'AGM'}
        return data

    @staticmethod
    def get_AGM_data(id):
        Parent = AGM.objects.get(id=id)
        all_members = DM.objects.filter(AGM_id=Parent)
        total_members = len(all_members) + 1
        total_sales = Parent.sales
        commission = Parent.commission
        for dm in all_members:
            total_sales += dm.sales
            commission += dm.commission
        data = {'Parent': Parent, 'Child': all_members, 'commission': commission,
                'total_member': total_members, 'total_sales': total_sales, 'type': 'DM'}
        return data

    @staticmethod
    def update_GM_sales(id):
        try:
            Parent = GM.objects.get(id=id)
            Parent.sales += 10
            Parent.commission += (10 * 100) * (25/100)
            Parent.save()
            all_rgms = RGM.objects.all()
            rgms_count = len(all_rgms)
            for rgm in all_rgms:
                rgm.commission += (10 * 100) * (15/100) * (1/rgms_count)
                rgm.save()
            all_agms = AGM.objects.all()
            agms_count = len(all_agms)
            for agm in all_agms:
                agm.commission += (10 * 100) * (10/100) * (1/agms_count)
                agm.save()

            all_dms = DM.objects.all()
            dms_count = len(all_dms)
            for dm in all_dms:
                dm.commission += (10 * 100) * (5/100) * (1/dms_count)
                dm.save()
        except Exception as ex:
            print(f"[!] {ex} [!]")
            return HttpResponse(f"Error:{ex}")

    @staticmethod
    def update_RGM_sales(id):
        try:
            Parent = RGM.objects.get(id=id)
            Parent.sales += 10
            Parent.save()

            all_agms = AGM.objects.filter(RGM_id=Parent)
            agms_count = len(all_agms)
            for agm in all_agms:
                agm.commission += (10 * 100) * (15/100) * (1/agms_count)
                agm.save()
                all_dms = DM.objects.filter(AGM_id=agm)
                dms_count = len(all_dms)
                for dm in all_dms:
                    dm.commission += (10 * 100) * (10/100) * (1/dms_count)
                    dm.save()
        except Exception as ex:
            print(f"[!] {ex} [!]")
            return HttpResponse(f"Error:{ex}")

    def update_AGM_sales(id):
        try:
            Parent = AGM.objects.get(id=id)
            Parent.sales += 10
            Parent.save()

            all_dms = DM.objects.filter(AGM_id=Parent)
            dms_count = len(all_dms)
            for dm in all_dms:
                dm.commission += (10 * 100) * (15/100) * (1/dms_count)
                dm.save()
        except Exception as ex:
            print(f"[!] {ex} [!]")
            return HttpResponse(f"Error:{ex}")

    @staticmethod
    def decrease_GM_sales(id):
        try:
            Parent = GM.objects.get(id=id)
            Parent.sales = 0 if Parent.sales <= 10 else Parent.sales - 10
            Parent.commission = 0 if Parent.commission <= 0 else Parent.commission - \
                (10 * 100) * (25/100)
            Parent.save()
            all_rgms = RGM.objects.all()
            rgms_count = len(all_rgms)
            for rgm in all_rgms:
                rgm.commission = 0 if rgm.commission <= 0 else rgm.commission - \
                    (10 * 100) * (15/100) * (1/rgms_count)
                rgm.save()
            all_agms = AGM.objects.all()
            agms_count = len(all_agms)
            for agm in all_agms:
                agm.commission = 0 if agm.commission <= 0 else agm.commission - \
                    (10 * 100) * (10/100) * (1/agms_count)
                agm.save()

            all_dms = DM.objects.all()
            dms_count = len(all_dms)
            for dm in all_dms:
                dm.commission = 0 if dm.commission <= 0 else dm.commission - \
                    (10 * 100) * (5/100) * (1/dms_count)
                dm.save()
        except Exception as ex:
            print(f"[!] {ex} [!]")
            return HttpResponse(f"Error:{ex}")

    @staticmethod
    def decrease_RGM_sales(id):
        try:
            Parent = RGM.objects.get(id=id)
            Parent.sales = 0 if Parent.sales <= 10 else Parent.sales - 10
            Parent.save()
            print('RGM updated---------------')
            all_agms = AGM.objects.filter(RGM_id=Parent)
            agms_count = len(all_agms)
            for agm in all_agms:
                agm.commission = 0 if agm.commission <= 0 else agm.commission - \
                    (10 * 100) * (15/100) * (1/agms_count)
                agm.save()
                all_dms = DM.objects.filter(AGM_id=agm)
                dms_count = len(all_dms)
                for dm in all_dms:
                    dm.commission = 0 if dm.commission <= 0 else dm.commission - \
                        (10 * 100) * (10/100) * (1/dms_count)
                    dm.save()
        except Exception as ex:
            print(f"[!] {ex} [!]")
            return HttpResponse(f"Error:{ex}")

    @staticmethod
    def decrease_AGM_sales(id):
        try:
            Parent = AGM.objects.get(id=id)
            Parent.sales = 0 if Parent.sales <= 10 else Parent.sales - 10
            Parent.save()
            all_dms = DM.objects.filter(AGM_id=Parent)
            dms_count = len(all_dms)
            for dm in all_dms:
                dm.commission = 0 if dm.commission <= 0 else dm.commission - \
                    (10 * 100) * (15/100) * (1/dms_count)
                dm.save()
            Parent.save()
        except Exception as ex:
            print(f"[!] {ex} [!]")
            return HttpResponse(f"Error:{ex}")

    @staticmethod
    def add_new_RGM(name,email,fk):
        try:
            Parent = GM.objects.get(id=fk)
            rgm = RGM.objects.create(
                GM_id=Parent, name=name, email=email, sales=0)
            rgm.save()
            print('[+] RGM added [+]')
        except Exception as ex:
            print(f"[!] {ex} [!]")
            return HttpResponse(f"Error:{ex}")

    @staticmethod
    def add_new_AGM(name,email,fk):
        try:
            rgm = RGM.objects.get(id=fk)
            agm = AGM.objects.create(
                RGM_id=rgm, name=name, email=email, sales=0)
            rgm.save()
            print('[+] AGM added [+]')
        except Exception as ex:
            print(f"[!] {ex} [!]")
            return HttpResponse(f"Error:{ex}")

    @staticmethod
    def add_new_DM(name,email,fk):
        try:
            rgm = AGM.objects.get(id=fk)
            agm = DM.objects.create(
                AGM_id=rgm, name=name, email=email, sales=0)
            rgm.save()
            print('[+] DM added [+]')
        except Exception as ex:
            print(f"[!] {ex} [!]")
            return HttpResponse(f"Error:{ex}")
