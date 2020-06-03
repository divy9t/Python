import xmlrpc.client as xmlrpclib
import datetime
import numpy as np

product_fields_to_pop = [
    'website_message_ids',
    'message_partner_ids',
    'public_categ_ids',
    'optional_product_ids',
    'packaging_ids',
    'sms_drawing',
    'attribute_line_ids',
    'website_meta_description',
    'sms_test',
    'website_size_y',
    'sms_related_part',
    'sms_ecoe',
    'property_valuation',
    'sms_eco_all_b',
    'sms_supplier_part',
    'hs_code',
    'product_image_ids',
    'availability',
    'sms_stock_value',
    'sms_whereused_d',
    'sms_on_order',
    'mo_count',
    'message_last_post',
    'sms_testb',
    'purchase_count',
    'sms_whereused_c',
    'property_cost_method',
    'sms_ecod',
    'sms_whereused_d_qty',
    'sms_supplier',
    'sms_leadtime',
    'sms_qty_forecast',
    'sms_product_date',
    'sms_cost',
    'website_size_x',
    'sms_supplierb',
    'website_description',
    'website_meta_keywords',
    'sms_deficit',
    'sms_ecoc',
    'property_account_creditor_price_difference',
    'website_sequence',
    'website_published',
    'rating_count',
    'sms_whereused_c_qty',
    'sms_eco_all',
    'website_meta_title',
    'sms_whereused_a',
    'purchase_line_warn',
    'availability_warning',
    'property_stock_account_output',
    'sms_related_parts',
    'sms_product_originator',
    'image_small',
    'accessory_product_ids',
    'track_service',
    'sms_use_bom_cost',
    'sms_description_picking',
    'alternative_product_ids',
    'sms_calculate_sale',
    'rating_last_value',
    'website_price',
    'item_ids',
    'sms_qty_stock',
    'image',
    'property_stock_account_input',
    'purchase_method',
    'sms_ecob',
    'sms_product_notes',
    'property_stock_procurement',
    'sms_whereused_all',
    'website_url',
    'sms_product_origin',
    'sms_cost_old',
    'rating_ids',
    'sms_whereused_b',
    'sms_whereused_b_qty',
    'website_price_difference',
    'warranty',
    'website_style_ids',
    'purchase_line_warn_msg',
    'sms_moq',
    'image_medium',
    'sms_ecoa',
    'sms_whereused_a_qty',
    'company_id',
    'message_follower_ids',
    'create_uid',
    'product_variant_ids',
    'message_ids',
    'taxes',
    'bom_ids'


]

tasks_otm_field = [
    'attachment_ids',
    'message_ids',
    'message_follower_ids'
]

tasks_fields_to_pop = [
    'sms_installed_systems',
    'date_start',
    'sms_time_on_task',
    'sms_date_started',
    'children_hours',
    'sms_child_task',
    'sms_parent_task_id',
    'sms_parent_task',
    'create_uid',
    'sms_date_stopped',
    'sms_stage_id', 'child_ids',
    'message_follower_ids',
    'rating_ids',
    'timesheet_ids',
    'message_ids',
    'notes',
    'sms_ncr_capa',
    'message_channel_ids',
    'message_last_post',
    'manager_id',
    'sms_installed_system',
    'subtask_project_id',
    'sms_service_request',
    'sms_related_ticket',
    'sale_line_id',
    'sms_child_task_complete',
    'delay_hours',
    'sms_customer',
    'procurement_id',
    'sms_user_id',
    'sms_messages_searched',
    'sms_ncr_cause',
    'write_uid',
    'partner_id',
    'company_id'
]

projects_to_retain_id = [

]

projects_field_to_pop = [
    'issue_ids',
    'balance',
    'percentage_satisfaction_task',
    'task_needaction_count',
    'sms_gantt_end',
    'use_issues',
    'tasks',
    'use_tasks',
    'label_issues',
    'issue_needaction_count',
    'project_count',
    'message_last_post',
    'line_ids',
    'message_follower_ids',
    'alias_model',
    'task_ids',
    'type_ids',
    'message_channel_ids',
    'message_partner_ids',
    'favorite_user_ids',
    'message_ids',
    'sms_gantt_start',
    'issue_count',
    'debit',
    'code',
    'tag_ids',
    'credit',
    'project_ids',
    'percentage_satisfaction_project'
]

sms_database = "SMS"
sms_password = "SmS12345&"
sms_url = "https://odoo.smsuk.co.uk/xmlrpc"
local_database = "SMSUAT"
local_password = "igCdvS1992xa"
local_url = "http://localhost:8069"
sms_username = "akarigo@surfacemeasurementsystems.com"
local_username = "smsodoo@surfacemeasurementsystems.com"

seperator = "\n====================================================\n"

sms_uid = xmlrpclib.ServerProxy(sms_url + '/common').login(sms_database, sms_username, sms_password)

sms_socket = xmlrpclib.ServerProxy("{0}/object".format(sms_url))

sms_model_socket = xmlrpclib.ServerProxy('{}/2/object'.format(sms_url))

local_uid = xmlrpclib.ServerProxy(local_url + '/xmlrpc/common').login(local_database, local_username, local_password)

local_socket = xmlrpclib.ServerProxy("{0}/xmlrpc/object".format(local_url))

old_id_mapping = {}

try:
    old_id_mapping = np.load('old_id_mapping.npy',allow_pickle='TRUE').item()
except:
    old_id_mapping = {}
    print("Data Dictionary for id not present")
print(local_socket)


def create_record(model, local_url, local_database, local_uid, local_password, data):
    models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(local_url))
    return models.execute_kw(local_database, local_uid, local_password, model, 'create', [data, ])


def write_record(model, local_url, local_database, local_uid, local_password, data, id):
    models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(local_url))
    return models.execute_kw(local_database, local_uid, local_password, model, 'write', [[id], data])


def search_by_name(model, local_url, local_database, local_uid, local_password, data):
    models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(local_url))
    model = model.split('.')
    model[0] = model[0] if not model[0] == 'sms' else model[0].replace('sms', 'ssms')
    model = '.'.join(model)
    if not model == 'mail.alias':
        return models.execute_kw(local_database, local_uid, local_password, model, 'search', [[['name', '=', data]]])
    else:
        return models.execute_kw(local_database, local_uid, local_password, model, 'search',
                                 [[['alias_name', '=', data]]])


def get_fields(sms_database, sms_uid, sms_password, socket_arg, model, args=[]):
    return socket_arg.execute(sms_database, sms_uid, sms_password, model, 'fields_get',
                              [], args)

def get_data_by_id(sms_socket,model, fields, sms_database, sms_uid, sms_password, ids):
    return sms_socket.execute_kw(sms_database, sms_uid, sms_password,model, 'read',ids, {'fields': fields})


def ge_local_fields(socket_arg, model, args=[]):
    return socket_arg.execute(local_database, local_uid, local_password, model, 'fields_get',
                              [], args)


def get_model_data(model_arg, model, operation, offset, limit, breakLimit, condition, fields):
    try:
        model_data = []
        if not fields:
            fields = get_fields(sms_database, sms_uid, sms_password, sms_socket, model, ['name', 'type', 'relation'])

        while True:
            print("In while loop for %s" % (model))

            data = model_arg.execute_kw(sms_database, sms_uid, sms_password,
                              model, operation,
                              [condition],
                              {'fields': fields,'context':{'lang':'en_GB'},'offset':offset ,'limit': limit})

            if data:
                print("Data Fetched for model %s"%(model))
                model_data.extend(data)
                offset = offset + limit
            else:
                print("No Data Available for model %s"%(model))
                break
        return model_data
    except:
        print("Something went wrong")
        return []


def get_local_model_data(socket_arg, model, operation, offset, limit, breakLimit, condition=[]):
    try:
        model_data = []
        fields = get_fields(local_database, local_uid, local_password, local_socket, model,
                            ['name', 'type', 'relation'])
        while True:
            print("In while loop for %s" % (model))
            data = socket_arg.execute(local_database, local_uid, local_password, model, operation, condition, fields,
                                      offset, limit)
            if data:
                print("Data Fetched for model %s"%(model))
                model_data.extend(data)
                offset = offset + limit
            else:
                print("No Data Available for model %s"%(model))
                break
        return model_data
    except Exception as e:
        print(e)
        return []


def get_model_list_arg(field_values=[]):
    return list(set(x['relation'] for x in list(field_values) if 'relation' in x))


def get_all_relational_data(models=[]):
    related_model_list = [x for x in models]
    for model in models:
        fields = get_model_list_arg(get_fields(sms_socket, model, ['name', 'type', 'relation']).values())
        related_model_list = list(set(related_model_list) | set(fields))
    return related_model_list


def create_project_relational_ids(modelData=[]):
    fields_to_exclude = ['write_uid', 'currency_id', 'analytic_account_id', 'user_id', 'create_uid', 'partner_id',
                         'company_id']
    mtoFieldsList = [x[0] for x in list(
        filter(lambda x: x[0][0] if x[1]['type'] == 'many2one' and x[0] not in fields_to_exclude else '',
               smsProjectFields.items()))]
    for data in modelData:
        iterRanger = list(data.keys())
        for key in iterRanger:
            if key in fields_to_exclude:
                data.pop(key)

            if key in mtoFieldsList and data[key]:
                relation = smsProjectFields[key]['relation']
                if  relation == "product.uom":
                    relation = 'uom.uom'

                if (not relation in old_id_mapping.keys()) and data[key]:
                    create_model_related_record(key, data, smsProjectFields)

                if data[key] and not data[key][0] in old_id_mapping[relation].keys():
                    create_model_related_record(key, data, smsProjectFields)

                if data[key]:
                    data[key] = old_id_mapping[relation][data[key][0]]
                    print("%s Relation Updated"%(smsProjectFields[key]['relation']))


def create_many2one_task_relation(taskData=[]):
    create_project_task_codes()
    mtoFieldsList = [x[0] for x in list(
        filter(lambda x: x[0][0] if x[1]['type'] == 'many2one' and x[0] not in tasks_fields_to_pop else '',
               smsProjectTaskFields.items()))]

    for data in taskData:
        for key, value in data.items():
            if key in mtoFieldsList:
                relation = smsProjectTaskFields[key]['relation']
                relation = relation.split('.')
                relation[0] = relation[0] if not relation[0] == 'sms' else relation[0].replace('sms', 'ssms')
                relation = '.'.join(relation)
                relation = smsProjectTaskFields[key]['relation']
                if (not relation in old_id_mapping.keys()) and data[key]:
                    create_model_related_record(key, data, smsProjectTaskFields)

                if data[key] and not data[key][0] in old_id_mapping[relation].keys():
                    create_model_related_record(key, data, smsProjectTaskFields)

                if data[key]:
                    try:
                        data[key] = old_id_mapping[relation][data[key][0]]
                    except Exception as e:
                        print(e)

def create_project_task_codes():
    menue = get_model_data(sms_model_socket, 'sms.menue', 'search_read', 0, 100, 100,[], ['name', 'descrip'])
    if 'ssms.menue' not in old_id_mapping.keys():
        old_id_mapping['ssms.menue'] = {}
    for menu in menue:
        existing = search_by_name('ssms.menue', local_url, local_database, local_uid, local_password, menu['name'])
        if not existing:
            new_id = create_record('ssms.menue', local_url, local_database, local_uid, local_password, menu)
            old_id_mapping['ssms.menue'].update({menu['id']: new_id})
        else:
            p = write_record('ssms.menue', local_url, local_database, local_uid, local_password, menu, existing[0])
            old_id_mapping['ssms.menue'].update({menu['id']: existing[0]})
            print(p)

    menul = get_model_data(sms_model_socket, 'sms.menul', 'search_read', 0, 100, 100, [], ['name', 'descrip'])
    if 'ssms.menul' not in old_id_mapping.keys():
        old_id_mapping['ssms.menul'] = {}
    for menu in menul:
        existing = search_by_name('ssms.menul', local_url, local_database, local_uid, local_password, menu['name'])
        if not existing:
            new_id = create_record('ssms.menul', local_url, local_database, local_uid, local_password, menu)
            old_id_mapping['ssms.menul'].update({menu['id']: new_id})
        else:
            p = write_record('ssms.menul', local_url, local_database, local_uid, local_password, menu, existing[0])
            old_id_mapping['ssms.menul'].update({menu['id']: existing[0]})
            print(p)

    menuk = get_model_data(sms_model_socket, 'sms.menuk', 'search_read', 0, 100, 100, [], ['name', 'descrip'])
    if 'ssms.menuk' not in old_id_mapping.keys():
        old_id_mapping['ssms.menuk'] = {}
    for menu in menuk:
        existing = search_by_name('ssms.menuk', local_url, local_database, local_uid, local_password, menu['name'])
        if not existing:
            new_id = create_record('ssms.menuk', local_url, local_database, local_uid, local_password, menu)
            old_id_mapping['ssms.menuk'].update({menu['id']: new_id})
        else:
            p = write_record('ssms.menuk', local_url, local_database, local_uid, local_password, menu, existing[0])
            old_id_mapping['ssms.menuk'].update({menu['id']: existing[0]})
            print(p)




def create_model_related_record(key, data={}, smsProjectFields={}):
    relation = smsProjectFields[key]['relation']
    if not relation in old_id_mapping.keys():
        old_id_mapping[relation] = {}
    print(key)
    print(data[key][1])

    if relation == 'mail.alias':
        relation_record = search_by_name(relation, local_url, local_database, local_uid, local_password,
                                         data[key][1].split('@')[0].strip())
    else:
        relation_record = search_by_name(relation, local_url, local_database, local_uid, local_password, data[key][1])

    if relation_record:
        print("Record Found %s" % (relation))
        relation_record = relation_record[0]

    if not relation_record:
        if relation == "mail.alias":
            relation_record = create_record(relation, local_url, local_database, local_uid,
                                            local_password, {'alias_name': data[key][1].split('@')[0],
                                                             'alias_model_id':
                                                                 search_by_name('ir.model', local_url,
                                                                                local_database,
                                                                                local_uid,
                                                                                local_password,
                                                                                "Lead/Opportunity")[0],
                                                             'alias_domain': data[key][1].split('@')[
                                                                 1]})
            print(relation_record)


        else:
            print(("Creating %s in %s model" % (data[key][1], relation)))

            partner_field = get_fields(sms_database, sms_uid, sms_password, sms_socket, relation,

                                       ['name', 'type', 'relation'])

            local_partner_fields = (ge_local_fields(local_socket, relation, ['name', 'type', 'relation']))

            partner_fields_to_remove = set(partner_field.keys()) - set(local_partner_fields.keys())

            present_data = get_model_data(sms_model_socket, relation, 'search_read', 0, 100, 100, [['id', '=', data[key][0]]],

                                          list(partner_field.keys()))

            if len(present_data) > 0:
                partner_data = present_data[0]
                partner_data['name'] = partner_data['name'].strip()
            else:
                partner_data = {'name': data[key][1]}

            partner_fields1 = [x[0] for x in list(

                filter(lambda x: x[0][0] if x[1]['type'] in ['many2one', 'one2many', 'many2many'] else '',

                       partner_field.items()))]

            partner_fields1.extend(list(partner_fields_to_remove))

            for field in partner_fields1:

                if field in partner_data.keys():
                    partner_data.pop(field)

            if relation == 'project.task.type':
                partner_data['legend_blocked'] = "Blocked"

                partner_data['legend_done'] = "Ready for Next Stage"

                partner_data['legend_normal'] = "In Progress"

            print(("Creating %s" % (partner_data['name'])))

            partner_data['name'] = partner_data['name'].strip()

            try:

                relation_record = create_record(relation, local_url, local_database, local_uid, local_password,
                                                partner_data)

                print(relation_record)

            except Exception as e:
                print(e)

    try:
        old_id_mapping[relation].update({data[key][0]: relation_record})
    except Exception as e:
        print(e)

def create_m2m_relation():
    for key, value in sms_related_tickets.items():
        try:
            if not key in old_id_mapping['project.task'].keys():
                continue
            new_id_list = [old_id_mapping['project.task'][x] for x in value]
            print(new_id_list)
            print(old_id_mapping['project.task'][key])
            models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(local_url))
            result = models.execute_kw(local_database, local_uid, local_password, 'project.task', 'write',
						  [[old_id_mapping['project.task'][key]], {'sms_related_tickets': [(6, 0, new_id_list)]}])
            print(result)
        except Exception as e:
            print(e)

def create_one2many_attachment(taskData=[]):
    try:
        for task in taskData:
            for key,value in task.items():
                if key == 'attachment_ids' and task[key]:
                    fields = ['name','type','datas','mimetype','res_model','res_id','res_name','description']
                    relation = smsProjectTaskFields[key]['relation']
                    attachments = []
                    for attachment_id in task[key]:
                        attachments.extend(get_data_by_id(sms_socket,relation,fields,sms_database,sms_uid,sms_password,[attachment_id]))
                    for data in attachments:
                        if data['res_id'] and old_id_mapping['project.task'][data['res_id']]:
                            data['res_id'] = old_id_mapping['project.task'][data['res_id']]
                            new_id = create_record(relation,local_url,local_database, local_uid, local_password, data )
                            print(new_id)
    except Exception as e:
        print(e)

def create_update_project_task(projectTaskData):
    for x in projectTaskData:
        try:
            task_id = get_local_model_data(local_socket, 'project.task', 'search_read', 0, 100, 100,
                                            [('old_id','=',x['id'])])
            if not 'project.task' in old_id_mapping.keys():
                old_id_mapping['project.task'] = {}

            temp_dict = {}
            temp_dict.update({'attachment_ids':x['attachment_ids']})
            x.pop('attachment_ids')

            if not task_id:
                x.update({'old_id': x['id']})
                new_id = create_record('project.task', local_url, local_database, local_uid, local_password, x)
                print("Project Task %s Created"%(x['name']))
                old_id_mapping['project.task'].update({x['id']: new_id})
                print(new_id)
            else:
                p = write_record('project.task', local_url, local_database, local_uid, local_password, x, task_id[0]['id'])
                if p:
                    print("Project Task %s updated"%(task_id[0]['name']))
                else:
                    print("Project Task %s updation failed"%(task_id[0]['name']))
                old_id_mapping['project.task'].update({x['id']: task_id[0]['id']})
                print(p)
            x.update(temp_dict)
            temp_dict = {}

        except Exception as e:
            print(e)


def create_eco_product_relation(product):
    try:
        new_eco_id_list = []
        if product['sms_eco_all_b']:
            for eco_id in product['sms_eco_all_b']:
                if old_id_mapping:
                    new_eco_id_list.append(old_id_mapping['project.task'][eco_id])
                else:
                    local_task_id = get_local_model_data(sms_socket, 'project.task', 'search_read', 0, 100, 100, [('old_id','=',eco_id)], [])
                    new_eco_id_list.append(local_task_id[0]['id'])

        product['previousEco'] = [(6, 0, new_eco_id_list)] if new_eco_id_list else []
        product.pop('sms_eco_all_b')
        return product
    except Exception as e:
        print(e)

def create_project_task_stages():
    project_task_stages = get_model_data(sms_model_socket, 'project.task.type', 'search_read', 0, 100, 100, [], [])
    if not 'project.task.type' in old_id_mapping.keys():
        old_id_mapping['project.task.type'] = {}

    for project_task_stage in project_task_stages:
        existing_stage_id = search_by_name('project.task.type',local_url, local_database, local_uid, local_password,project_task_stage['name'])
        project_task_stage.pop('mail_template_id')
        project_task_stage.pop('rating_template_id')
        if not project_task_stage['legend_blocked']:
            project_task_stage['legend_blocked'] = "Blocked"

        if not project_task_stage['legend_done']:
            project_task_stage['legend_done'] = "Ready for Next Stage"

        if not project_task_stage['legend_normal']:
            project_task_stage['legend_normal'] = "In Progress"

        new_project_ids = [old_id_mapping['project.project'][x] for x in project_task_stage['project_ids'] if
                           x in old_id_mapping['project.project'].keys()]
        project_task_stage['project_ids'] = [(6, 0, new_project_ids)]

        if not existing_stage_id:
            new_stage_id = create_record('project.task.type', local_url, local_database, local_uid, local_password,
                                         project_task_stage)
            print("%s stage id is %s"%(project_task_stage['name'],new_stage_id))
            old_id_mapping['project.task.type'].update({project_task_stage['id']: new_stage_id})

        else:
            p = write_record('project.task.type', local_url, local_database, local_uid, local_password, project_task_stage,
                         existing_stage_id[0])
            if p:
                old_id_mapping['project.task.type'].update({project_task_stage['id']: existing_stage_id[0]})
            print("Project stage %s updated"%(project_task_stage['name']))


def create_uoms():
    uom_categories = get_model_data(sms_model_socket, 'product.uom.categ', 'search_read', 0, 100, 100, [], [])
    if not 'uom.category' in old_id_mapping.keys():
        old_id_mapping['uom.category'] = {}
    for uom_category in uom_categories:
        uom_category_id = search_by_name('uom.category',local_url, local_database, local_uid, local_password,uom_category['name'])
        if not uom_category_id:
            new_categ_id = create_record('uom.category', local_url, local_database, local_uid, local_password,
                          uom_category)
            old_id_mapping['uom.category'].update({uom_category['id']:new_categ_id})
        else:
            old_id_mapping['uom.category'].update({uom_category['id']: uom_category_id[0]})
    uoms = get_model_data(sms_model_socket, 'product.uom', 'search_read', 0, 100, 100, [], [])
    if not 'uom.uom' in old_id_mapping.keys():
        old_id_mapping['uom.uom'] = {}
    uom_type_dict = {'bigger':[],'smaller':[],'reference':[]}

    for uom in uoms:
        uom_type_dict[uom['uom_type']].append(uom)

    for uom in uom_type_dict['reference']:
        uom_name = uom['name']
        if uom_name == 'Litre(s)':
            uom_name = 'Liters'
        if uom_name == 'Day(s)':
            uom_name = 'Days'
        uom_id = search_by_name('uom.uom',local_url, local_database, local_uid, local_password,uom_name)
        if not uom_id:
            uom['category_id'] = old_id_mapping['uom.category'][uom['category_id'][0]]
            if uom['name'] == '500':
                uom['uom_type'] = 'smaller'
                uom['factor'] = 5
            if uom['name'] == "Each":
                uom['uom_type'] = 'smaller'
                uom['factor'] = 5

            new_uom_id = create_record('uom.uom', local_url, local_database, local_uid, local_password,
                                       uom)
            old_id_mapping['uom.uom'].update({uom['id']: new_uom_id})
        else:
            print("Data Present")
            old_id_mapping['uom.uom'].update({uom['id']:uom_id[0]})

    for uom in uom_type_dict['smaller']:
        uom_id = search_by_name('uom.uom',local_url, local_database, local_uid, local_password,uom['name'])
        if not uom_id:
            uom['category_id'] = old_id_mapping['uom.category'][uom['category_id'][0]]
            print(uom)
            new_uom_id = create_record('uom.uom', local_url, local_database, local_uid, local_password,
                                       uom)
            old_id_mapping['uom.uom'].update({uom['id']: new_uom_id})
        else:
            print("Data Present")
            old_id_mapping['uom.uom'].update({uom['id']:uom_id[0]})

    for uom in uom_type_dict['bigger']:
        uom_id = search_by_name('uom.uom',local_url, local_database, local_uid, local_password,uom['name'])
        if not uom_id:
            uom['category_id'] = old_id_mapping['uom.category'][uom['category_id'][0]]
            print(uom)
            new_uom_id = create_record('uom.uom', local_url, local_database, local_uid, local_password,
                                       uom)
            old_id_mapping['uom.uom'].update({uom['id']: new_uom_id})
        else:
            print("Data Present")
            old_id_mapping['uom.uom'].update({uom['id']:uom_id[0]})

def create_product_vendor_mapping(product):
    if product['seller_ids']:
        suppler_info_fields = get_fields(sms_database, sms_uid, sms_password, sms_socket, 'product.supplierinfo',
                                             ['name', 'type', 'relation'])
        sellers_data = []

        for seller_id in product['seller_ids']:
            seller_info = {}
            seller_data = get_data_by_id(sms_socket,'product.supplierinfo',list(suppler_info_fields.keys()),sms_database,sms_uid,sms_password,[seller_id])
            if not seller_data:
                continue

            currency = False
            if seller_data[0]['currency_id'][1] in old_id_mapping['res.currency'].keys():
                print("Currency Found in dict")
                currency = old_id_mapping['res.currency'][seller_data[0]['currency_id'][1]]
            if not currency:
                continue

            seller_info['currency_id'] = currency
            contact = False
            if seller_data[0]['name'][0] in old_id_mapping['res.partner'].keys():
                print("Vendor Found in dict")
                contact = old_id_mapping['res.partner'][seller_data[0]['name'][0]]

            if not contact:
                continue

            seller_info['name'] = contact
            seller_info['product_name'] = seller_data[0]['product_name']
            seller_info['product_code'] = seller_data[0]['product_code']
            seller_info['delay'] = seller_data[0]['delay']
            seller_info['min_qty'] = seller_data[0]['min_qty']
            seller_info['price'] = seller_data[0]['price']
            seller_info['date_start'] = seller_data[0]['date_start']
            seller_info['date_end'] = seller_data[0]['date_end']
            sellers_data.append((0,0,seller_info))
            print("Added seller no %s"%(product['name']))
        product['seller_ids'] = sellers_data

def prepare_bom_lines(bom):
    prepared_lines = []
    for bom_line_id in bom['bom_line_ids']:
        bom_line = get_model_data(sms_model_socket, 'mrp.bom.line', 'search_read', 0, 100, 100, [['id','=',bom_line_id]], [])
        if not bom_line:
            continue

        bom_line_product_template = [x for x in productData if x['product_variant_id'] == bom_line[0]['product_id']]

        if not bom_line_product_template:
            continue

        bom_line_product = get_local_model_data(local_socket, 'product.template', 'search_read', 0, 100, 100,
                                        [('id','=',old_id_mapping['product.template'][bom_line_product_template[0]['id']])])
        if not bom_line_product:
            continue

        bom_line[0]['product_id'] = bom_line_product[0]['product_variant_id'][0]
        bom_line[0]['product_uom_id'] = old_id_mapping['uom.uom'][bom_line[0]['product_uom_id'][0]]

        bom_line[0].pop('write_uid')
        bom_line[0].pop('attribute_value_ids')
        bom_line[0].pop('sms_bomline_draw')
        bom_line[0].pop('sms_bomline_on_order')
        bom_line[0].pop('sms_line_cost')
        bom_line[0].pop('sms_bomline_deficit')
        bom_line[0].pop('sms_bom_product_image')
        bom_line[0].pop('sms_location')
        bom_line[0].pop('sms_bom_stock')
        bom_line[0].pop('sms_cost_bom')
        bom_line[0].pop('sms_bom_comp_ref')
        bom_line[0].pop('child_bom_id')
        bom_line[0].pop('create_uid')
        bom_line[0].pop('bom_id')
        bom_line[0].pop('child_line_ids')
        bom_line[0].pop('has_attachments')
        bom_line[0].pop('sms_bom_location')
        prepared_lines.append((0,0,bom_line[0]))
    bom['bom_line_ids'] = prepared_lines

def create_bom_data(bomIds):
    try:
        boms = np.load('liveBom.npy', allow_pickle='TRUE')
    except Exception as e:
        boms = []

    if len(boms) <= 0:
        boms = get_model_data(sms_model_socket, 'mrp.bom', 'search_read', 0, 100, 100, [], [])
        np.save('liveBom.npy', boms)

    for bom in boms:
        try:
            existing_bom = get_local_model_data(local_socket, 'mrp.bom', 'search_read', 0, 100, 100,
                                                [('old_id', '=', bom['id'])])
            if bom['id'] in bomIds:
                if not existing_bom:
                    temp_bom = {}
                    temp_bom['product_tmpl_id'] = old_id_mapping['product.template'][bom['product_tmpl_id'][0]]
                    temp_bom['code'] = bom['code']
                    temp_bom['sms_lock_bom'] = bom['sms_lock_bom']
                    temp_bom['product_uom_id'] = old_id_mapping['uom.uom'][bom['product_uom_id'][0]]
                    temp_bom['product_qty'] = bom['product_qty']
                    temp_bom['type'] = bom['type']
                    temp_bom['sequence'] = bom['sequence']
                    temp_bom['old_id'] = bom['id']
                    prepare_bom_lines(bom)
                    temp_bom['bom_line_ids'] = bom['bom_line_ids']

                    if not 'mrp.bom' in old_id_mapping.keys():
                        old_id_mapping['mrp.bom'] = {}

                    new_bom = create_record('mrp.bom', local_url, local_database, local_uid, local_password,
                                                temp_bom)
                    old_id_mapping['mrp.bom'].update({temp_bom['old_id']: new_bom})
                    print("New BOM ID %s"%(new_bom))
                else:
                    print("BOM already exists")
        except Exception as e:
            print("Exception Occured")
            print(e)


def create_next_previous_revisions(productData):
    for product in productData:
        try:
            temp_prod = {}
            product['nextRevision'] = False
            if product['sms_next_revision']:
                if old_id_mapping['product.template'][product['sms_next_revision'][0]]:
                    temp_prod['nextRevision'] = old_id_mapping['product.template'][product['sms_next_revision'][0]]
            product.pop('sms_next_revision')

            product['previousRevision'] = False
            if product['sms_previous_revision']:
                if old_id_mapping['product.template'][product['sms_previous_revision'][0]]:
                    temp_prod['previousRevision'] = old_id_mapping['product.template'][product['sms_previous_revision'][0]]
            product.pop('sms_previous_revision')

            if temp_prod:
                if 'seller_ids' in product.keys():
                    product.pop('seller_ids')
                if 'price' in product.keys():
                    product.pop('price')
                product_updated = write_record('product.template', local_url, local_database, local_uid, local_password, temp_prod,
                                               old_id_mapping['product.template'][product['id']])
                if product_updated:
                    print("Product Updated")
                else:
                    print("product Revision Updation Failed")
        except Exception as e:
            print("Exception Occured!")
            print(e)


def remove_product_fields(product):
    for field in product_fields_to_pop:
        if field in product.keys():
            product.pop(field)
    return product

def create_partner_currency_dict():
    partners = get_local_model_data(local_socket, 'res.partner', 'search_read', 0, 100, 100,
                                        [('old_id','!=',False)])
    print(len(partners))
    if 'res.partner' not in old_id_mapping.keys():
        old_id_mapping['res.partner'] = {}
    for partner in partners:
        old_id_mapping['res.partner'].update({partner['old_id']:partner['id']})

    currencies = get_local_model_data(local_socket, 'res.currency', 'search_read', 0, 100, 100,
                                        ['|',('active','=',True),('active','=',False)])
    print(len(currencies))

    if not 'res.currency' in old_id_mapping.keys():
        old_id_mapping['res.currency'] = {}

    for currency in currencies:
        old_id_mapping['res.currency'].update({currency['name']:currency['id']})

def create_taxes_dict():
    local_taxes = get_local_model_data(local_socket, 'account.tax', 'search_read', 0, 100, 100,[])
    sms_taxes = get_model_data(sms_model_socket, 'account.tax', 'search_read', 0, 100, 100, [], [])


    if not 'account.tax' in old_id_mapping.keys():
        old_id_mapping['account.tax'] = {}

    [old_id_mapping['account.tax'].update({sms_tax['id']:local_tax['id']}) for local_tax in local_taxes for sms_tax in sms_taxes if sms_tax['description'].strip() == local_tax['description'].strip()]


def create_route_dict():
    local_routes = get_local_model_data(local_socket, 'stock.location.route', 'search_read', 0, 100, 100, [])
    sms_routes = get_model_data(sms_model_socket, 'stock.location.route', 'search_read', 0, 100, 100, [], [])
    if not 'sms.location.route' in old_id_mapping.keys():
        old_id_mapping['stock.location.route'] = {}

    [old_id_mapping['stock.location.route'].update({sms_route['id']:local_route['id']}) for local_route in local_routes for sms_route in sms_routes if local_route['name'].strip() == sms_route['name'].strip()]

def map_product_fields(product_wizard_dict, productData):
    create_partner_currency_dict()
    create_taxes_dict()
    create_route_dict()
    productData = list(map( create_eco_product_relation , productData))
    for product in productData:
        if 'product.category' not in old_id_mapping.keys():
            old_id_mapping['product.category'] = {}


        if product:
            if not product['categ_id'][0] in old_id_mapping['product.category'].keys():
                categ = get_local_model_data(local_socket, 'product.category', 'search_read', 0, 100, 100, [('display_name','=',product['categ_id'][1])])
                old_id_mapping['product.category'].update({product['categ_id'][0]:categ[0]['id']})
    
            product['name'] = product['name'].strip()
            product['taxes_id'] = [(6,0,[old_id_mapping['account.tax'][x] for x in product['taxes_id'] if x in old_id_mapping['account.tax'].keys()])]
            product['supplier_taxes_id'] = [(6, 0, [old_id_mapping['account.tax'][x] for x in product['supplier_taxes_id'] if x in old_id_mapping['account.tax'].keys()])]
        
            product['categ_id'] = old_id_mapping['product.category'][product['categ_id'][0]]
            product['currency_id'] = product['currency_id'][0]
            product['route_ids'] = [(6,0,[old_id_mapping['stock.location.route'][x] for x in product['route_ids'] if x in old_id_mapping['stock.location.route'].keys()])]
            product['list_price'] = product['website_public_price']
            product.pop('website_public_price')
            product['standard_price'] = product['sms_cost']
            product.pop('sms_cost')
            product['image_1920'] = product['image_medium']
            product.pop('image_medium')
            product['image_128'] = product['image_small']
            product.pop('image_small')
            product['image_1024'] = product['image']
            product['property_stock_production'] = 15
            product['property_stock_inventory'] = 14
            product.pop('image')
            product['old_id'] = product['id']
            product['uom_id'] = old_id_mapping['uom.uom'][product['uom_id'][0]]
            product['uom_po_id'] = old_id_mapping['uom.uom'][product['uom_po_id'][0]]
            if product['bom_ids']:
                bom_ids.extend(product['bom_ids'])
            if product['default_code'] in product_wizard_dict.keys():
                product['Title'] = product_wizard_dict[product['default_code']]['notes']
                product['Specification'] = product_wizard_dict[product['default_code']]['notes_specs']
            remove_product_fields(product)
            create_product_vendor_mapping(product)
            create_update_local_products([product])
    return productData

def create_update_local_products(product_data):
    for prod in product_data:
        try:
            product_id = get_local_model_data(local_socket, 'product.template', 'search_read', 0, 100, 100,
                                        [('old_id','=',prod['id'])])
            if not 'product.template' in old_id_mapping.keys():
                old_id_mapping['product.template'] = {}
            print("Creating/ Updating Product %s"%(prod['name']))


            temp_dict = {}
            temp_dict['sms_next_revision'] = prod['sms_next_revision']
            temp_dict['sms_previous_revision'] = prod['sms_previous_revision']
            prod.pop('sms_next_revision')
            prod.pop('sms_previous_revision')
            temp_dict['product_variant_id'] = prod['product_variant_id']
            prod.pop('product_variant_id')

            if not product_id:
                new_id = create_record('product.template', local_url, local_database, local_uid, local_password,
                                       prod)

                old_id_mapping['product.template'].update({prod['id']: new_id})
                print(new_id)
            else:
                prod.pop('seller_ids')
                prod.pop('price')

                p = write_record('product.template', local_url, local_database, local_uid, local_password, prod,product_id[0]['id'])

                old_id_mapping['product.template'].update({prod['id']: product_id[0]['id']})
                print("Product Already Present")
            prod.update(temp_dict)
           
            temp_dict = {}
        except Exception as e:
            print(e)


def get_product_variant_data(wizardOptions):
    for wizardOption in wizardOptions:
        variant = False
        if wizardOption['required']:
            variant = get_model_data(sms_model_socket, 'product.product', 'search_read', 0, 100, 100, [['id','=',wizardOption['required'][0]]], ['name','barcode','default_code'])

        wizardOption['required'] = variant
    return wizardOptions

def create_wizard_option_dict(wizardOption):
    wizard_dict = {}
    for data in wizardOption:
        if data['required']:
            wizard_dict[data['required'][0]['default_code']] = data

    return  wizard_dict

# Working Code for product category migration and uom
categoryFields = get_fields(sms_database, sms_uid, sms_password, sms_socket, 'product.category',
                            ['name', 'type', 'relation'])
categoryData = get_model_data(sms_model_socket, 'product.category', 'search_read', 0, 100, 100, [],
                              list(categoryFields.keys()))

parent_category_id = ''
parent_categ_id = search_by_name('product.category', local_url, local_database, local_uid, local_password,'All')
if not parent_categ_id:
    parent_category_id = create_record('product.category', local_url, local_database, local_uid, local_password, "All")
else:
    parent_category_id = parent_categ_id[0]
if not 'product.category' in old_id_mapping.keys():
    old_id_mapping['product.category'] = {}

for x in categoryData:
    category = search_by_name('product.category', local_url, local_database, local_uid, local_password, x['name'])
    if not category:
        x.pop('property_account_creditor_price_difference_categ')
        x.pop('parent_right')
        x.pop('child_id')
        x.pop('parent_left')
        for key, value in x.items():
            if categoryFields[key]['type'] == 'many2one':
                if key == "parent_id":
                    x[key] = parent_category_id
                else:
                    x[key] = x[key][0] if x[key] else []

        child_id = create_record('product.category', local_url, local_database, local_uid, local_password, x)
        old_id_mapping['product.category'].update({x['id']:child_id})
        print("Category %s created"%(x['name']))
    else:
        old_id_mapping['product.category'].update({x['id']: category[0]})
        print("Category %s already present"%(x['name']))

print(seperator)

create_uoms()

print(seperator)

# Working code for the project and ECO's
smsProjectFields = get_fields(sms_database, sms_uid, sms_password, sms_socket, 'project.project',
                              ['name', 'type', 'relation'])
for x, y in smsProjectFields.items():
    for key, value in y.items():
        if key == "relation" and value == "product.uom":
            value = "uom.uom"


try:
    projectData = np.load('liveProjectData.npy',allow_pickle='TRUE')
except Exception as e:
    projectData = []

if len(projectData) <= 0:
    projectData = get_model_data(sms_model_socket, 'project.project', 'search_read', 0, 100, 100, [], [])
    np.save('liveProjectData.npy', projectData)

for project in projectData:
    project['vtenContact'] = False
    if project['partner_id']:
        project['vtenContact'] = project['partner_id'][1]
    project.pop('partner_id')

if not 'project.project' in old_id_mapping.keys():
    old_id_mapping['project.project'] = {}

for y in projectData:
    list(map(lambda x: y.pop(x), projects_field_to_pop))

create_project_relational_ids(projectData)

print(len(projectData))
for x in projectData:
    try:
        project = get_local_model_data(local_socket, 'project.project', 'search_read', 0, 100, 100,
                                            [('old_id','=',x['id'])])
        if not project:
            x.pop('alias_model') if 'alias_model' in x.keys() else ''
            x.update({'old_id':x['id']})
            p = create_record('project.project', local_url, local_database, local_uid, local_password, x)
            old_id_mapping['project.project'].update({x['id']:p})
            print(p)
        else:
            old_id_mapping['project.project'].update({x['id']: project[0]['id']})
            print("Project %s Present"%(project[0]['name']))
    except Exception as e:
        print(e)

print(seperator)

create_project_task_stages()

print(seperator)

Working Code for project task
smsProjectTaskFields = get_fields(sms_database, sms_uid, sms_password, sms_socket, 'project.task',
                              ['name', 'type', 'relation'])

try:
    projectTaskData = np.load('liveProjectTaskData.npy',allow_pickle='TRUE')
except Exception as e:
    projectTaskData = []

if len(projectTaskData) <= 0:
    projectTaskData = get_model_data(sms_model_socket, 'project.task', 'search_read', 0, 100, 100, [], [])
    np.save('liveProjectTaskData.npy', projectTaskData)

count = 0
for task in projectTaskData:
    if task['user_id']:
        task['vtenContact'] = task['user_id'][1]
        count += 1
    task.pop('user_id')
print(count)

sms_related_tickets = {x['id']: x['sms_related_tickets'] for x in projectTaskData if x['sms_related_tickets']}
print(len(projectTaskData))
m2mFields = [x[0] for x in list(
        filter(lambda x: x[0][0] if x[1]['type'] == 'many2many' and x[0] not in tasks_fields_to_pop else '',
               smsProjectTaskFields.items()))]

tasks_fields_to_pop.extend(m2mFields)

for y in range(len(projectTaskData)):
    list(map(lambda x: projectTaskData[y].pop(x),tasks_fields_to_pop))
    temp = {}
    for key,value in projectTaskData[y].items():
        if key == 'sms_time_started':
            temp['planned_date_begin'] = value

        if key == 'sms_time_stopped':
            temp['planned_date_end'] = value
    if 'planned_date_end' in temp.keys() and temp['planned_date_end']:
        if isinstance(temp['planned_date_end'], str):
            temp['planned_date_end'] = str(datetime.datetime.strptime(temp['planned_date_end'], '%Y-%m-%d %H:%M:%S') + datetime.timedelta(seconds=2))
        else:
            temp['planned_date_end'] = str(temp['planned_date_end'] + datetime.timedelta(seconds=2))

    if ('planned_date_end' and 'planned_date_begin' in temp.keys()) and temp['planned_date_end'] and temp['planned_date_begin'] and temp['planned_date_begin'] > temp['planned_date_end']:
        temp['planned_date_begin'], temp['planned_date_end'] = temp['planned_date_end'], temp['planned_date_begin']

    projectTaskData[y].pop('sms_time_started')
    projectTaskData[y].pop('sms_time_stopped')
    projectTaskData[y].update(temp)
    temp = {}

create_many2one_task_relation(projectTaskData)

create_update_project_task(projectTaskData)
np.save('old_id_mapping.npy', old_id_mapping)
old_id_mapping = np.load('old_id_mapping.npy',allow_pickle='TRUE').item()
print("Creating Attachments")
print(seperator)
#create_one2many_attachment(projectTaskData)
print(seperator)
create_m2m_relation()
print(seperator)
print(count)
#Product Migration Code
smsProductFields = get_fields(sms_database, sms_uid, sms_password, sms_socket, 'product.template',
                              ['name', 'type', 'relation'])
try:
    productData = np.load('liveProductData.npy',allow_pickle='TRUE')
except Exception as e:
    productData = []

if len(productData) <= 0:
    productData = get_model_data(sms_model_socket, 'product.template', 'search_read', 0, 100, 100, [],
                                 list(smsProductFields.keys()))
    np.save('liveProductData.npy', productData)

try:
    wizardOption = np.load('liveWizardOption.npy',allow_pickle='TRUE')
except Exception as e:
    wizardOption = []

if len(wizardOption)<=0:
    wizardOptionField = get_fields(sms_database, sms_uid, sms_password, sms_socket, 'sms.wizardoptions',
                                   ['name', 'type', 'relation'])

    wizardOption = get_model_data(sms_model_socket, 'sms.wizardoptions', 'search_read', 0, 100, 100, [],
                                  list(wizardOptionField.keys()))
    wizardOption = get_product_variant_data(wizardOption)
    np.save('liveWizardOption.npy', wizardOption)


product_wizard_dict = create_wizard_option_dict(wizardOption)
bom_ids = []
productData = map_product_fields(product_wizard_dict, productData)

np.save('old_id_mapping.npy', old_id_mapping)
print(seperator)
create_next_previous_revisions(productData)
print(seperator)
productData = np.load('liveProductData.npy',allow_pickle='TRUE')
create_bom_data(bom_ids)
print(seperator)
np.save('old_id_mapping.npy', old_id_mapping)
