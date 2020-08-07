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
sms_password = "akarigo@123"
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
    old_id_mapping = np.load('old_id_mapping.npy', allow_pickle='TRUE').item()
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


def get_data_by_id(sms_socket, model, fields, sms_database, sms_uid, sms_password, ids):
    return sms_socket.execute_kw(sms_database, sms_uid, sms_password, model, 'read', ids, {'fields': fields})


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
                                        {'fields': fields, 'context': {'lang': 'en_GB'}, 'offset': offset,
                                         'limit': limit})

            if data:
                print("Data Fetched for model %s" % (model))
                model_data.extend(data)
                offset = offset + limit
            else:
                print("No Data Available for model %s" % (model))
                break
        return model_data
    except Exception as e:
        print(e)
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
                print("Data Fetched for model %s" % (model))
                model_data.extend(data)
                offset = offset + limit
            else:
                print("No Data Available for model %s" % (model))
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
                if relation == "product.uom":
                    relation = 'uom.uom'

                if (not relation in old_id_mapping.keys()) and data[key]:
                    create_model_related_record(key, data, smsProjectFields)

                if data[key] and not data[key][0] in old_id_mapping[relation].keys():
                    create_model_related_record(key, data, smsProjectFields)

                if data[key]:
                    data[key] = old_id_mapping[relation][data[key][0]]
                    print("%s Relation Updated" % (smsProjectFields[key]['relation']))


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
    menue = get_model_data(sms_model_socket, 'sms.menue', 'search_read', 0, 100, 100, [], ['name', 'descrip'])
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

            present_data = get_model_data(sms_model_socket, relation, 'search_read', 0, 100, 100,
                                          [['id', '=', data[key][0]]],

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
                                       [[old_id_mapping['project.task'][key]],
                                        {'sms_related_tickets': [(6, 0, new_id_list)]}])
            print(result)
        except Exception as e:
            print(e)


def create_product_attachments():
    fields = ['name', 'type', 'datas', 'mimetype', 'res_model', 'res_id', 'res_name', 'description']
    attachments = get_model_data(sms_model_socket, 'ir.attachment', 'search_read', 0, 100, 100,
                                 [['res_model', '=', 'product.template']], fields)
    print(len(attachments))
    for attachment in attachments:
        if attachment['res_id'] and (attachment['res_id'] in old_id_mapping['product.template'].keys()) and \
                old_id_mapping['product.template'][attachment['res_id']]:
            attachment['res_id'] = old_id_mapping['product.template'][attachment['res_id']]
            new_id = create_record('ir.attachment', local_url, local_database, local_uid, local_password, attachment)
            print(new_id)
        else:
            print("The exp id %s"%(attachment['res_id']))


def create_one2many_attachment(taskData=[]):
    try:
        for task in taskData:
            for key, value in task.items():
                if key == 'attachment_ids' and task[key]:
                    fields = ['name', 'type', 'datas', 'mimetype', 'res_model', 'res_id', 'res_name', 'description']
                    relation = smsProjectTaskFields[key]['relation']
                    attachments = []
                    for attachment_id in task[key]:
                        attachments.extend(
                            get_data_by_id(sms_socket, relation, fields, sms_database, sms_uid, sms_password,
                                           [attachment_id]))
                    for data in attachments:
                        if data['res_id'] and old_id_mapping['project.task'][data['res_id']]:
                            data['res_id'] = old_id_mapping['project.task'][data['res_id']]
                            new_id = create_record(relation, local_url, local_database, local_uid, local_password, data)
                            print(new_id)
    except Exception as e:
        print(e)


def create_update_project_task(projectTaskData):
    for x in projectTaskData:
        try:
            task_id = get_local_model_data(local_socket, 'project.task', 'search_read', 0, 100, 100,
                                           [('old_id', '=', x['id'])])
            if not 'project.task' in old_id_mapping.keys():
                old_id_mapping['project.task'] = {}

            temp_dict = {}
            temp_dict.update({'attachment_ids': x['attachment_ids']})
            x.pop('attachment_ids')

            if not task_id:
                x.update({'old_id': x['id']})
                new_id = create_record('project.task', local_url, local_database, local_uid, local_password, x)
                print("Project Task %s Created" % (x['name']))
                old_id_mapping['project.task'].update({x['id']: new_id})
                print(new_id)
            else:
                p = write_record('project.task', local_url, local_database, local_uid, local_password, x,
                                 task_id[0]['id'])
                if p:
                    print("Project Task %s updated" % (task_id[0]['name']))
                else:
                    print("Project Task %s updation failed" % (task_id[0]['name']))
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
                    local_task_id = get_local_model_data(sms_socket, 'project.task', 'search_read', 0, 100, 100,
                                                         [('old_id', '=', eco_id)], [])
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
        existing_stage_id = search_by_name('project.task.type', local_url, local_database, local_uid, local_password,
                                           project_task_stage['name'])
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
            print("%s stage id is %s" % (project_task_stage['name'], new_stage_id))
            old_id_mapping['project.task.type'].update({project_task_stage['id']: new_stage_id})

        else:
            p = write_record('project.task.type', local_url, local_database, local_uid, local_password,
                             project_task_stage,
                             existing_stage_id[0])
            if p:
                old_id_mapping['project.task.type'].update({project_task_stage['id']: existing_stage_id[0]})
            print("Project stage %s updated" % (project_task_stage['name']))


def create_uoms():
    uom_categories = get_model_data(sms_model_socket, 'product.uom.categ', 'search_read', 0, 100, 100, [], [])
    if not 'uom.category' in old_id_mapping.keys():
        old_id_mapping['uom.category'] = {}
    for uom_category in uom_categories:
        uom_category_id = search_by_name('uom.category', local_url, local_database, local_uid, local_password,
                                         uom_category['name'])
        if not uom_category_id:
            new_categ_id = create_record('uom.category', local_url, local_database, local_uid, local_password,
                                         uom_category)
            old_id_mapping['uom.category'].update({uom_category['id']: new_categ_id})
        else:
            old_id_mapping['uom.category'].update({uom_category['id']: uom_category_id[0]})
    uoms = get_model_data(sms_model_socket, 'product.uom', 'search_read', 0, 100, 100, [], [])
    if not 'uom.uom' in old_id_mapping.keys():
        old_id_mapping['uom.uom'] = {}
    uom_type_dict = {'bigger': [], 'smaller': [], 'reference': []}

    for uom in uoms:
        uom_type_dict[uom['uom_type']].append(uom)

    for uom in uom_type_dict['reference']:
        uom_name = uom['name']
        if uom_name == 'Litre(s)':
            uom_name = 'Liters'
        if uom_name == 'Day(s)':
            uom_name = 'Days'
        uom_id = search_by_name('uom.uom', local_url, local_database, local_uid, local_password, uom_name)
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
            old_id_mapping['uom.uom'].update({uom['id']: uom_id[0]})

    for uom in uom_type_dict['smaller']:
        uom_id = search_by_name('uom.uom', local_url, local_database, local_uid, local_password, uom['name'])
        if not uom_id:
            uom['category_id'] = old_id_mapping['uom.category'][uom['category_id'][0]]
            print(uom)
            new_uom_id = create_record('uom.uom', local_url, local_database, local_uid, local_password,
                                       uom)
            old_id_mapping['uom.uom'].update({uom['id']: new_uom_id})
        else:
            print("Data Present")
            old_id_mapping['uom.uom'].update({uom['id']: uom_id[0]})

    for uom in uom_type_dict['bigger']:
        uom_id = search_by_name('uom.uom', local_url, local_database, local_uid, local_password, uom['name'])
        if not uom_id:
            uom['category_id'] = old_id_mapping['uom.category'][uom['category_id'][0]]
            print(uom)
            new_uom_id = create_record('uom.uom', local_url, local_database, local_uid, local_password,
                                       uom)
            old_id_mapping['uom.uom'].update({uom['id']: new_uom_id})
        else:
            print("Data Present")
            old_id_mapping['uom.uom'].update({uom['id']: uom_id[0]})


def create_product_vendor_mapping(product):
    if product['seller_ids']:
        suppler_info_fields = get_fields(sms_database, sms_uid, sms_password, sms_socket, 'product.supplierinfo',
                                         ['name', 'type', 'relation'])
        sellers_data = []

        for seller_id in product['seller_ids']:
            seller_info = {}
            seller_data = get_data_by_id(sms_socket, 'product.supplierinfo', list(suppler_info_fields.keys()),
                                         sms_database, sms_uid, sms_password, [seller_id])
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
            sellers_data.append((0, 0, seller_info))
            print("Added seller no %s" % (product['name']))
        product['seller_ids'] = sellers_data


def prepare_bom_lines(bom):
    prepared_lines = []
    for bom_line_id in bom['bom_line_ids']:
        bom_line = get_model_data(sms_model_socket, 'mrp.bom.line', 'search_read', 0, 100, 100,
                                  [['id', '=', bom_line_id]], [])
        if not bom_line:
            continue

        bom_line_product_template = [x for x in productData if x['product_variant_id'] == bom_line[0]['product_id']]

        if not bom_line_product_template:
            continue

        bom_line_product = get_local_model_data(local_socket, 'product.template', 'search_read', 0, 100, 100,
                                                [('id', '=', old_id_mapping['product.template'][
                                                    bom_line_product_template[0]['id']])])
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
        prepared_lines.append((0, 0, bom_line[0]))
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
                    print("New BOM ID %s" % (new_bom))
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
                    temp_prod['previousRevision'] = old_id_mapping['product.template'][
                        product['sms_previous_revision'][0]]
            product.pop('sms_previous_revision')

            if temp_prod:
                if 'seller_ids' in product.keys():
                    product.pop('seller_ids')
                if 'price' in product.keys():
                    product.pop('price')
                product_updated = write_record('product.template', local_url, local_database, local_uid, local_password,
                                               temp_prod,
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
                                    [('old_id', '!=', False)])
    print(len(partners))
    if 'res.partner' not in old_id_mapping.keys():
        old_id_mapping['res.partner'] = {}
    for partner in partners:
        old_id_mapping['res.partner'].update({partner['old_id']: partner['id']})

    currencies = get_local_model_data(local_socket, 'res.currency', 'search_read', 0, 100, 100,
                                      ['|', ('active', '=', True), ('active', '=', False)])
    print(len(currencies))

    if not 'res.currency' in old_id_mapping.keys():
        old_id_mapping['res.currency'] = {}

    for currency in currencies:
        old_id_mapping['res.currency'].update({currency['name']: currency['id']})


def create_taxes_dict():
    local_taxes = get_local_model_data(local_socket, 'account.tax', 'search_read', 0, 100, 100, [])
    sms_taxes = get_model_data(sms_model_socket, 'account.tax', 'search_read', 0, 100, 100, [], [])

    if not 'account.tax' in old_id_mapping.keys():
        old_id_mapping['account.tax'] = {}

    [old_id_mapping['account.tax'].update({sms_tax['id']: local_tax['id']}) for local_tax in local_taxes for sms_tax in
     sms_taxes if sms_tax['description'].strip() == local_tax['description'].strip()]


def create_route_dict():
    local_routes = get_local_model_data(local_socket, 'stock.location.route', 'search_read', 0, 100, 100, [])
    sms_routes = get_model_data(sms_model_socket, 'stock.location.route', 'search_read', 0, 100, 100, [], [])
    if not 'sms.location.route' in old_id_mapping.keys():
        old_id_mapping['stock.location.route'] = {}

    [old_id_mapping['stock.location.route'].update({sms_route['id']: local_route['id']}) for local_route in local_routes
     for sms_route in sms_routes if local_route['name'].strip() == sms_route['name'].strip()]


def map_product_fields(product_wizard_dict, productData):
    create_partner_currency_dict()
    create_taxes_dict()
    create_route_dict()
    productData = list(map(create_eco_product_relation, productData))
    for product in productData:
        if 'product.category' not in old_id_mapping.keys():
            old_id_mapping['product.category'] = {}

        if product:
            if not product['categ_id'][0] in old_id_mapping['product.category'].keys():
                categ = get_local_model_data(local_socket, 'product.category', 'search_read', 0, 100, 100,
                                             [('display_name', '=', product['categ_id'][1])])
                old_id_mapping['product.category'].update({product['categ_id'][0]: categ[0]['id']})

            product['name'] = product['name'].strip()
            product['taxes_id'] = [(6, 0, [old_id_mapping['account.tax'][x] for x in product['taxes_id'] if
                                           x in old_id_mapping['account.tax'].keys()])]
            product['supplier_taxes_id'] = [(6, 0,
                                             [old_id_mapping['account.tax'][x] for x in product['supplier_taxes_id'] if
                                              x in old_id_mapping['account.tax'].keys()])]

            product['categ_id'] = old_id_mapping['product.category'][product['categ_id'][0]]
            product['currency_id'] = product['currency_id'][0]
            product['route_ids'] = [(6, 0, [old_id_mapping['stock.location.route'][x] for x in product['route_ids'] if
                                            x in old_id_mapping['stock.location.route'].keys()])]
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

            if product['default_code']:
                product['default_code'], product['version'] = product['default_code'].split('Rev.')[0], \
                                                              product['default_code'].split('Rev.')[1] if len(
                                                                  product['default_code'].split('Rev.')) > 1 else 0

            if product['bom_ids']:
                bom_ids.extend(product['bom_ids'])
            if product['default_code'] and product['default_code'] in product_wizard_dict.keys():
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
                                              [('old_id', '=', prod['id'])])
            if not 'product.template' in old_id_mapping.keys():
                old_id_mapping['product.template'] = {}
            print("Creating/ Updating Product %s" % (prod['name']))

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

                p = write_record('product.template', local_url, local_database, local_uid, local_password, prod,
                                 product_id[0]['id'])

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
            variant = get_model_data(sms_model_socket, 'product.product', 'search_read', 0, 100, 100,
                                     [['id', '=', wizardOption['required'][0]]], ['name', 'barcode', 'default_code'])

        wizardOption['required'] = variant
    return wizardOptions


def create_wizard_option_dict(wizardOption):
    wizard_dict = {}
    for data in wizardOption:
        if data['required']:
            wizard_dict[data['required'][0]['default_code']] = data

    return wizard_dict

def mark_serialized_product():
    products = get_model_data(sms_model_socket, 'product.template', 'search_read', 0, 100, 100,
                                     [['sms_test', 'ilike', 'yes']], ['id','sms_test'])
    i = 1
    for product in products:
        product_id = get_local_model_data(local_socket, 'product.template', 'search_read', 0, 100, 100,
                                              [('old_id', '=', product['id'])])
        if product_id:
            p = write_record('product.template', local_url, local_database, local_uid, local_password, {'tracking':'serial'},
                         product_id[0]['id'])

            if p:
               print("Product Marked as serialized")

            i += 1
            print(i)

        else:
            print("Product doesn't exists")


    print(len(products))


ids = [7685,5369,179,8,9,4719,4441,6384,6955,5166,6377,6956,6029,3252,4224,4871,4872,249,5823,10,3115,3248,5958,3335,253,630,11,4500,7665,8077,8079,12,8544,5009,255,13,256,8037,7805,14,6019,6020,3493,3498,6710,7232,7610,7375,7376,367,368,7121,7655,5645,861,6718,4456,3171,3183,15,6106,5307,5774,4703,6693,6064,6203,7911,150,152,6670,7843,6625,937,3505,6024,5565,5566,373,8221,5816,5342,5265,3873,3994,3996,4006,4014,4019,4022,5007,4730,4731,4160,3187,7976,5532,3875,4024,4030,4035,381,7889,7537,17,145,7327,3188,981,979,3191,5236,4532,288,289,4720,5579,5580,290,292,293,284,285,4773,5605,5597,296,8003,4830,5401,524,525,5904,4769,5336,7878,6298,257,3442,7581,3495,7695,498,412,6672,18,19,7582,7719,298,6900,7538,747,6092,4881,7904,287,8209,4628,5471,460,300,5005,3067,5260,3294,5003,3599,20,5524,5078,4594,7845,3195,4822,21,690,989,5126,4528,303,7207,6909,6908,613,5251,7406,7405,6913,6286,7856,6200,8036,7026,5128,6910,7163,5956,7145,6394,7378,8069,7135,7488,305,8473,339,4068,3762,3651,3713,6702,5077,3269,8130,8243,5263,6089,735,5444,226,6033,532,6229,3654,5310,6889,6338,6988,7623,22,5319,6172,5204,6700,4040,7044,7045,6365,3876,4015,4037,5717,3045,5316,5837,281,6053,7214,506,4668,8047,6180,6182,7115,23,7075,3238,6948,327,572,570,6040,871,575,576,577,424,4956,422,6904,24,691,7715,8200,7561,25,5748,5749,699,346,347,6743,3340,7284,8110,8109,6275,7872,7587,4878,6284,8228,5725,4048,765,4377,6240,6688,6681,156,3377,4186,5811,7261,7246,4379,5002,7248,26,7030,27,7757,7814,8102,7233,7234,5900,349,4971,6223,6221,5232,455,456,5332,203,619,6279,620,5395,416,217,207,888,896,6668,5851,7963,8157,3324,3492,997,6747,7272,4386,4421,7083,7189,7615,7440,148,898,6022,7420,8040,389,715,718,721,6530,6729,7306,7379,6270,5771,7370,6505,29,5906,4589,4588,6346,4468,4966,7853,3767,3770,7624,5785,118,30,5536,6714,6928,7021,7333,7034,7592,7625,7329,6997,551,7331,31,5386,6514,3274,5834,354,6881,578,580,5812,579,6151,7467,341,3214,3021,975,3037,3072,3176,3179,3300,3227,963,3224,3121,3062,3192,3028,3221,3097,7436,3119,3049,32,7404,3180,3099,3139,935,3156,2998,355,356,534,3658,7227,5472,357,5030,279,6149,5224,5275,6062,7195,199,7661,7442,3098,6259,4553,6277,3181,3034,3198,3178,3203,6615,7344,994,5866,7744,8559,7745,528,710,5448,3068,6257,7576,7352,193,614,8022,8021,4778,3019,3092,3168,3090,5898,358,591,5546,7862,3614,3615,7425,5586,5585,7616,810,5588,6661,7596,5287,7598,5286,5284,3682,7597,6198,5115,5888,6349,5561,5845,5847,8128,5860,5780,6049,5431,5966,4765,6986,3161,7694,3122,34,4811,5508,878,5992,3167,7506,7507,5466,7736,594,35,3351,3353,6056,8088,6651,3786,3787,36,6184,4188,5971,6991,7589,6992,136,6187,5776,7539,509,5438,4994,37,686,7428,7430,7429,377,6046,6047,7141,5713,6215,6623,374,7455,4725,4211,4962,166,6840,590,7358,7614,764,4444,38,7916,5853,8562,4745,6219,39,555,4690,6140,5321,4954,5222,783,7758,5257,7858,3877,4028,40,5797,5501,5798,6363,6620,4817,7978,3656,8024,6137,5397,5899,4066,6038,41,3265,6123,42,5186,5183,5553,5559,6498,5832,4739,4742,175,6013,6078,258,182,184,43,44,3277,758,7474,8138,6626,925,4785,3439,6018,6323,6119,6280,6548,7422,5228,7255,7103,6318,6759,7316,4355,6004,4212,45,5328,3133,678,6637,3878,4018,7402,376,6632,6147,6155,380,536,7503,8167,537,3280,5516,3892,4873,7682,4652,3677,3676,4217,5935,385,7007,5908,7167,8075,6194,7604,7882,160,8137,8198,780,7868,615,7810,8204,802,7786,8181,695,3148,540,543,5116,7492,6406,47,557,788,371,7816,6400,7766,951,955,953,4384,5773,886,4230,6727,689,7980,6863,641,5564,3361,3362,507,4828,48,49,3881,4004,3246,3244,3069,274,7447,3264,5022,5694,7974,7981,5818,7594,7983,8059,7089,7095,6322,6342,8649,3336,3337,516,386,4726,5243,7790,6305,391,7521,6810,6273,8114,7142,5821,7058,7567,982,983,50,626,6379,5418,7036,7407,7906,3032,3023,3070,432,3445,3499,163,5943,3704,7590,8107,51,6750,5796,7175,7176,5339,4222,5174,800,750,6870,6763,5954,5953,7346,8098,8100,6370,4759,4712,4538,4713,7212,6005,6007,7883,6614,3338,6460,5929,8139,850,3306,5949,4342,863,864,3326,7942,7852,5910,7411,6707,7252,7278,7253,6617,7257,6517,7283,7263,6051,3164,383,3271,7612,6255,7051,4059,3647,4579,4580,7373,5335,3775,4320,5814,6160,6161,52,4791,3105,3017,3005,6372,493,8160,4740,5892,8120,6205,6206,366,3695,3694,3696,6876,8532,6738,4555,6675,3435_1,3486_1,4852,6642,454,6590,8025,8118,8625,171,8134,8533,7617,5534,5515,930,6872,4795,595,3883,5712,4005,7096,6922,6983,6995,6984,6985,5041,7660,3698,6124,6663,4453,4214,6586,5921,7382,4577,4578,3359,5417,3116,7061,7132,8081,5460,8141,6898,8276,7654,6188,5176,6930,5283,6612,7289,3780,3785,7139,7118,6525,3438_1,3484_1,3488_1,3491_1,7825,7826,3374,4403,6523,4743,4818,3679,7707,7706,7708,5924,5925,6213,139,53,54,3518,3691,3687,5382,1000,6579,3365,3364,7841,7241,235,6657,3341,3342,601,6533,5937,8083,797,5338,3366,3185,128,5425,4770,55,5289,8013,56,5517,713,714,7770,7771,6217,6896,7179,57,73,4921,4103,5764,477,8070,277,6249,7133,6376,7017,556,608,7264,7265,6628,6630,58,7450,7451,7673,59,60,61,915,5539,6320,5061,8530,7881,5356,5069,5233,6512,6511,7335,157,158,5024,7105,5130,7493,7494,402,7476,5110,7354,5779,6002,6316,6227,6315,6503,4591,361,3215,8214,5894,5410,6208,7449,5989,8031,977,6035,5648,8041,63,4632,4633,4834,4835,3219,7522,3089,6919,866,8125,6057,514,4728,7733,4820,396,4868,64,3375,4889,672,674,5551,7680,131,8150,188,7628,4231,530,65,6139,3674,4360,6926,365,4604,6144,6253,5000,83,66,5249,3272,221,359,116,5922,7824,3126,3124,3142,2997,933,5815,2994,3056,3082,3173,3085,3200,3029,3196,3602,3091,3047,3044,5722,2985,3145,5721,3132,3127,3061,3605,3064,3051,3022,3123,3170,3065,7099,67,596,597,868,918,6723,4927,5440,143,768,5995,5996,5997,5993,8105,7181,7182,6509,7065,612,3572,5468,3669,3570,7579,7458,4893,6621,6592,6583,6690,68,3050,4970,7389,7820,6381,69,5507,4782,8043,7000,6999,7013,7113,403,702,5828,5835,6655,467,4968,782,6527,71,6894,7415,5365,3705,5361,72,907,6916,8085,4692,8027,6127,8067,7738,7866,6232,791,4875,6699,7417,653,7361,7363,5366,5371,5883,688,4887,5368,362,7704,4780,74,5402,996,75,4845,5071,927,6383,6584,3771,7040,7295,6117,5849,3884,4001,3109,587,7748,545,544,7038,7432,472,471,5826,3287,8219,194,283,5059,195,4171,7462,592,6711,518,5867,633,632,5441,5442,4381,7951,7952,3716,8126,5650,554,7985,3016,5778,7674,574,6288,6289,6290,6271,7396,7397,7023,76,821,6480,5960,5961,5772,741,4530,4847,4848,7902,3482_1,3483_1,3485_1,3487_1,3489_1,495_1,7930,3259,3260,3261,77,78,79,680,4747,80,434,7711,4996,5522,3765,669,4814,670,4813,4330,4891,3712,4890,6671,7469,5072,447,81,769,5819,4550,4688,4689,4973,4536,5933,749,6902,704,5046,725,3020,6932,7047,7588,8428,8065,8195,82,8033,5521,6643,6247,5348,7136,5398,4046,6683,628,84,7194,3666,425,4636,3703,5422,3379,3330,7074,5053,5423,4788,3237,7802,6884,337,4793,6044,6507,4992,4643,7543,6692,561,7637,448,5795,3650,3086,4729,3184,336,6293,4738,5234,5235,86,87,6405,5124,6977,693,667,3266,7751,7752,7860,7434,7545,7077,6331,6076,7864,7934,3101,7066,6976,760,8171,5096,398,7712,7633,7877,7360,8482,6398,7714,6725,7496,7497,4864,90,62,3532,3540,894,7355,4057,8226,363,469,809,91,684,4922,6652,88,5081,6114,5164,5854,7464,7161,5747,6633,4693,5067,3626,5482,6647,8086,7678,5969,892,5093,6251,6635,3239,3240,6940,7063,205,5343,92,93,497,6282,3347,3348,600,4709,7124,4124,5914,5492,7101,5148,431,7898,7899,7900,311,428,306,102,310,312,104,105,106,241,7541,107,4100,259,6093,501,785,108,443,451,6873,6543,94,4508,5256,621,789,503,109,7486,7571,427,639,7158,698,7461,185,6761,8154,5084,5086,7204,711,247,5660,7546,125,154,5381,110,111,6924,7806,7024,3230,426,112,167,687,8011,500,5025,114,115,5201,4987,6231,5105,209,7490,776,777,778,169,7523,7774,7960,3367,773,444,550,7721,6042,836,834,835,5942,246,375,95,8063,6827,642,582,697,6000,5998,6545,8210,5317,96,6224,6996,6236,3606,7908,7304,3257,5026,5554,5782,752,753,4220,6388,7219,4691,7217,5262,5411,3692,410,6107,3885,4012,3536,3088,692,3515,3516,3517,5855,6914,7435,7188,3443,3497,7394,7238,6659,97,8152,482,7743,3283,900,7081,3279,7080,6358,8019,8018,8534,3494,6157,6521,6179,5902,3598,4990,230,3702,4784,3701,4105,6003,4356,4095,5896,5548,3158,8073,3253,3255,3254,682,5470,7400,832,837,5886,6740,568,6942,5582,3286,6970,7524,822,364,6327,6697,5428,538,487,539,488,7107,3152,3620,2993,3004,922,3146,3616,3618,3621,3157,3177,7281,3118,3622,7287,3609,3619,3010,3603,3031,6304,3002,3193,3041,3617,3169,6695,5308,599,4551,5064,3661,3664,4697,3250,6165,6789,4460,6677,903,4620,6138,617,990,986,5809,991,5584,387,731,548,8206,3683,3684,4592,6890,5474,7754,7753,7003,7530,3627,8328,7011,406,8104,7409,8090,5278,3886,4007,4036,5162,5304,520,521,510,5719,6080,7364,6233,7225,3096,6936,5291,5802,4458,4044,5875,7266,7267,5313,3649,3322,6087,4382,6500,4388,4863,7286,4373,3754,4833,8144,8146,8145,7073,4375,7053,7005,7147,7015,7144,7514,7457,7151,6121,6353,8116,6487,6334,7259,7606,7605,5388,3329,7028,8331,6581,5113,4771,737,5011,8132,4016,6110,8263,6109,3888,4017,4027,4029,4031,7338,7700,6361,3147,993,3153,5331,5373,7186,5646,7574,7735,3999,4000,7793,616,603,6927,604,7116,7117,650,7313,479,480,4003,7465,7499,6474,244,238,7847,852,830,3893,3992,4787,3997,660,7828,6081,8208,7348,7749,7293,7600,6296,3009,957,2996,3084,969,6515,3059,3611,967,3612,3600,961,3052,3130,3607,3151,3194,7940,8053,5800,5452,4988,4586,909,912,911,3043,5324,3159,910,973,3155,3112,3102,3163,3613,3104,3197,3149,3114,3131,949,8028,5104,7652,8217,882,8175,5768,683,3190,3012,3567,6519,491,3372,490,3225,3223,3046,3610,3343,3063,3502,3520,3160,3508,7697,6541,7137,7777,6878,484,7128,4102,7127,3078,3048,4501,3150,6303,3141,3608,3053,3007,3033,3138,3008,4338,947,3182,3024,7202,5884,4345,5364,7602,5489,709,7836,7837,3296,6906,928,7222,98,99,7779,7563,6341,6344,6340,6343,6774,6177,6314,875,4733,4650,965,5323,679,6238,5734,3350,7078,4824,5948,7445,4774,4775,5549,5145,5146,7568,7570,8168,7569,3083,4705,7750,5562,369,4938,588,5462,6028,5751,5753,855,856,3534,3533,6026,5416,806,5715,3357,5528,6083,4369,5806,8038,4870,6591,7291,122,4603,4667,5915,5842,644,6994,745,744,7870,8091,100,6173]

def create_contact_attachments(ids):
    fields = ['name', 'type', 'datas', 'mimetype', 'res_model', 'res_id', 'res_name', 'description']
    attachments = get_model_data(sms_model_socket, 'ir.attachment', 'search_read', 0, 100, 100,
                                 ['&',['res_id','in',ids],['res_model', '=', 'res.partner']], fields)
    print(len(attachments))
    total = 0
    for attachment in attachments:
        contact = get_local_model_data(local_socket, 'res.partner', 'search_read', 0, 100, 100,
                                              [('old_id', '=', attachment['res_id'])])
        if contact:
            attachment['res_id'] = contact[0]['id']
            new_id = create_record('ir.attachment', local_url, local_database, local_uid, local_password, attachment)
            print("New Attachment Id %s"%(new_id))
            total += 1
        else:
            print("Contact doesn't exist")
    print("The total of %s attachments are imported"%(total))

create_contact_attachments(ids)
