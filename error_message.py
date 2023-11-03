from enum import Enum


class MessageEnum(Enum):
    successs = 0, "成功"
    login_username_not_message = 100001, "用户名没有输入"
    login_password_not_message = 100002, '密码没有输入'
    login_user_inactivatesd = 100003, '用户未激活,请联系管理员激活'
    login_user_free_message = 100004, '用户冻结！'
    login_user_is_login = 100005, '用户已经登录'
    login_user_sucess_message = 0, '登录成功！'
    login_user_fremm = 100007, "密码错误超过5次，请十分钟后登录"
    login_password_error_message = 100008, '密码错误'
    login_user_not_exict_message = 100009, '用户不存在'
    activi_user_jobnum = 100010, '用户工号唯一'
    activi_user_jobnum_is = 100011, '用户工号已经激活'
    interface_add_success = 100012, '添加成功'
    interface_add_erroe = 100013, '添加接口失败,请从新添加'
    request_null_message = 100014, '没有发送数据'
    testeveirment_not_exict = 100015, '没有找到测试环境'
    project_not_exict = 100016, '无法找到项目'
    request_success = 100017, '请求成功'
    password_not_same = 100018, '请确认两次密码输入是否一致'
    email_geshi_error = 100019, '邮箱格式错误'
    jobnum_oblg_reg_one = 100020, '用户工号只能注册一次'
    user_exict = 100021, '用户名已经存在'
    email_exict = 100022, '邮箱已经注册'
    common_is_same = 100023, '通用配置的名称必须唯一'
    common_gene_not_support = 100024, '通用配置的类型暂时不支持'
    common_is_not_exict = 100025, '编辑的通用配置不存在，请确定'
    common_edit_is_success = 100026, '通用配置编辑成功'
    re_is_same = 100027, '操作的名称必须唯一'
    case_not_exict = 100028, '测试用例不存在'
    re_is_not_exitc = 100029, '操作的类型不支持'
    re_editisnot = 100030, '编辑操作不存在'
    change_password_success = 100031, '修改密码成功'
    change_password_error = 100032, '修改密码失败'
    user_reset_owner = 100033, '自己不能重置自己的密码'
    user_reset_isnot_amin = 100034, '不是管理员不能重置'
    user_reset_error = 100035, '重置密码失败'
    reset_success_message = 100036, '已经重置！密码：111111'
    permiss_is_ness = 100037, '权限不足'
    user_is_not_free = 100038, '用户没有处于冻结状态'
    activ_is_int = 100039, "工号为数字"
    user_is_un_free = 100040, '解冻成功'
    ower_not_free_me = 100041, '自己不能解冻自己'
    user_is_unfree_success = 100042, '解冻失败'
    free_user_error = 100043, '冻结用户失败！'
    free_is_success = 100044, '已经冻结成功'
    ower_cannot_free_me = 100045, '自己不能冻结自己'
    free_is_again = 100046, '已经冻结,无需再次冻结'
    admin_cannot_use = 100047, '自己不能取消自己的管理员'
    user_email_not_none = 100048, '邮箱不能为空'
    user_email_error = 100049, '邮箱格式错误'
    user_register_error = 100050, '注册失败'
    parames_not_null = 100051, '参数缺少'
    select_project_not = 100052, '请选择项目'
    super_admin_not_set_project = 100053, '超级管理员不用设置项目'
    set_project_bot_exict = 100054, '设置的项目不存在或者已经删除'
    set_fail = 100055, '设置管理失败'
    set_is_admin = 100056, '你已经是项目管理员了，不需要再次设置'
    project_admin_many = 100057, '单个项目的管理员已经达到后台设置的个数限制'
    set_project_admin_exception = 100058, '设置过程目前存在异常'
    not_add_project = 100059, '不能不添加测试项目'
    project_not_case = 100060, '亲你见过只有测试项目没有测试用例的测试任务吗'
    task_update_case = 100061, '任务更新用例成功'
    task_update_case_error = 100062, '任务更新用例失败'
    task_must_be_mulite_case = 10063, '定时任务执行过程的测试用例为多用例，请你谅解'
    task_start_success = 100064, "定时任务启动成功"
    task_start_eeor = 100065, '定时任务启动失败'
    task_stop_fail = 100066, '定时任务暂停成功'
    task_repuse_success = 100067, '定时任务恢复成功'
    task_repuse_fail = 100068, '定时任务恢复失败！已经为您初始化'
    remove_success = 100069, '定时任务移除成功！'
    remove_fail = 100070, '定时任务移除失败！已经为您初始化'
    project_search = 100071, '项目查询不到'
    project_delet_free = 100072, '项目已经删除或者冻结'
    delete_not_exict = 100073, '删除的不存在'
    task_is_delete = 100074, '已经删除'
    task_delete_success = 100075, '删除任务成功'
    task_delete_fail = 100076, '删除任务出现异常，系统已经为你还原'
    task_edit = 100077, '编辑成功'
    task_edit_fail = 100078, '编辑失败'
    task_name_not_none = 100079, '任务名不能为空！'
    task_recevier = 100080, '接受人邮件不能为空！'
    task_user = 100081, '维护人邮件不能为空！'
    task_edit_not_exict = 100082, '你编辑的不存在'
    task_event_not_exict = 100083, '任务的测试环境不存在'
    task_name_not_same = 100084, '任务名不能重复'
    task_project_is_not_exict = 100085, '任务的所属项目不存在'
    task_add_fail = 100086, '任务添加失败'
    use_select_edit = 100087, '请重新选择编辑的mock'
    mock_check_again = 100088, '请重新选择编辑的mock'
    mock_edit_fail = 100089, '编辑出现状况'
    mock_start_success = 100090, 'mock开启成功，可以正常使用'
    mock_start_error = 100091, 'mock的服务开启失败，因为不存在'
    mock_server_start_fail = 100091, 'mock开启失败'
    mock_close_success = 100092, 'mock关闭成功,停止访问'
    mock_server_close_fail = 100093, 'mock开启失败'
    mock_stop_fail = 100094, 'mock的服务关闭失败，因为不存在或者已经删除'
    edit_interface = 100095, '要编辑的接口不存在'
    edit_interface_null_parame = 100096, '请确定各项参数都正常填写'
    Interface_edit = 100097, '编辑成功'
    Interface_edit_fail = 100098, '编辑失败'
    import_max_big = 100099, '系统目前支持的导入有限制，请分开导入'
    import_project_not_exitc = 100100, '找不到项目，请确定导入的项目是否存在'
    import_model = 100101, '找不到模块不存在！，请确定导入的项目是否存在'
    import_success = 100102, '导入成功'
    import_fail = 100103, '导入失败，请检查文件'
    import_fail_admin = 100104, '导入失败，请联系管理员'
    add_parame_interface = 100105, '添加参数的接口不存在'
    export_fail = 100106, '导出失败！'
    interface_add_not = 100107, '删除接口不存在'
    delete_inteface_error = 100108, '删除接口失败'
    delete_case_error = 100109, '删除用例失败'
    user_is_exict = 100110, '用户已经存在！不能重复!'
    delete_fail = 100111, '删除失败'
    testeveirment_use_one_nam = 100112, '测试环境必须是相互独立的'
    add_case_erro = 100113, '添加测试用例失败'
    mock_name_only_one = 100114, 'mockserver的名称不能重复'
    add_mock_exception = 100115, '创建新的mock接口出错'
    config_not_exict = 100116, '配置已经删除或者不存在'
    cobfig_delete_error = 100117, '删除配置失败！'
    error_send_message = 100118, '没有发送数据'
    edit_mock_error = 100119, '编辑失败'
    delete_mock_error = 100120, '删除失败，找不到mocksever'
    create_mock_error = 100121, '创建新的mock接口出错'
    edit_model_error = 100122, '编辑模块出现问题'
    model_only_one = 100123, '模块不能重复存在'
    model_edit_fial = 100124, '添加失败'
    model_not_exict = 100125, '模块不存在'
    eidt_excption = 100126, '编辑出现问题'
    email_only_one = 100127, '邮箱已经存在！请选个邮箱!'
    delete_report_fail = 100128, '删除测试报告失败！'
    delete_report_not_exict = 100129, '删除的测试报告不存在'
    project_only_one = 100130, '项目不能重复'
    user_not_permision = 100131, '权限不足！'
    project_cannot_empty = 100132, '项目名称不能为空！'
    project_add_error = 100133, '项目添加失败'
    Interface_not_exict = 100134, '要查看的接口不存在'
    parame_name_not_empty = 100135, '参数的名字不能为空'
    parame_error = 100136, '参数格式类型必须填写进去'
    parame_is_exict = 100137, '参数名称已经存在于该接口'
    parame_is_not_exict = 100138, '不存在的参数'
    parame_type_is_not_empty = 100139, '参数格式类型必须填写进去'
    edit_fial = 100140, '编辑出错'
    case_many_to_select = 100141, '请选择一个以上的用例来执行'
    select_event = 100142, '请选择测试环境'
    run_only_one_project = 100143, '目前单次只能执行一个项目的用例'
    send_email_fali = 100144, '发送邮件失败，请检查您默认的邮件设置是否正确'
    send_email_success = 100145, '测试已经完成，并且给您默认设置发送了测试报告'
    send_fail_oneuser = 100146, '无法完成，需要去您的个人设置去设置一个默认的邮件发送'
    send_dingtlak_success = 100147, '测试报告已经发送钉钉讨论群，测试报告已经生成'
    send_dingtalk_error = 100148, '测试报告发送钉钉讨论群失败！请检查相关配置！'
    test_case_success = 100149, '测试已经完成，测试报告已经生成'
    test_error = 100150, '测试失败'
    test_case = 100151, '请确定你要测试的用例是否存在！'
    get_reply_data_fail = 100152, '获取依赖数据失败'
    test_feild = 100153, '测试参数应该是字典格式！'
    assert_not_in_or_sql_not_in = 100154, '要判断数据库但是没有找到数据库的语句或者断言的字段'
    test_sql_url_not_in = 100155, '测试环境数据库url配置不存在'
    test_sql_port_not_in = 100156, '测试环境数据库port配置不存在'
    test_sql_host_not_in = 100157, '测试环境数据库host配置不存在'
    test_sql_login_user_not_in = 100158, '测试环境数据库登录user配置不存在'
    test_sql_login_user_password_not_in = 100159, '测试环境数据库登录密码配置不存在'
    test_sql_repy_sql_feild = 100160, '依赖数据库必须有字段'
    test_sql_connect_sql_error = 100161, '链接数据库出现问题'
    test_sql_query_error = 100162, '查询数据库出现问题'
    change_parames_faild = 100163, '转化请求参数失败'
    test_case_run_error = 100164, '测试用例测试失败,请检查用例！'
    test_case_run_pass = 100165, '测试用例执行通过'
    test_case_run_fail = 100166, '测试用例测试失败,请检查用例！'
    test_case_requesst_exception = 100167, '测试返回异常，,请检查用例！'
    test_run_fail_not_support = 100168, '目前还不支持你所选择的类型的协议'
    your_change_export_project_not_exict = 100169, '你选择导出接口的项目不存在'
    your_export_interface_fail = 100170, '导出接口失败'
    not_find_your_case = 100171, '没有找到你需要的测试用例'
    you_case_not_try = 100172, '您的测试用例没有在任何环境调试过'
    Incorrect_format = 100173, '格式不正确'
    test_server_not_exict = 100174, '测试服务器不存在'
    case_to_jmx_case_fail = 100175, '转换接口压测测试用例失败'
    case_jmx_not_excit = 100176, '测试脚本不存在'
    case_jmx_not_select_server = 100177, '测试脚本没有选择服务器'
    case_test_sever_not_exict = 100178, '测试服务器不存在或者已经删除'
    case_jmx_run_seccess = 100179, '压测已经在远程服务器运行'
    case_to_jmx_success = 100180, '转化接口压测用例成功'
    reply_must_be_repy_flied = 100181, '选择依赖后必须填写获取依赖的接口的字段'
    must_be_every_parame = 100182, '请准确填写用例的各项信息'
    save_test_result_error = 100183, '选择保存测试结果出现异常'
    action_not_exict = 100184, '操作不存在'
    case_edit_error = 100185, '测试用例编辑失败'
    request_method = -1, '请求方式错误'
    resquest_return_not_json = -2, '你写入的返回不能正常json！请检查'
    request_method_not_supprot = -2, '你写入的类型目前系统不支持'
    method_parame_not_right = -4, '你输入的参数不正确'
    request_scre = -3, '安全校验失败!'
    requests_case_interface_not_exit = 100190, '获取用例的时候，接口不存在'
    requests_case_project_not_exit = 100191, '获取用例的时候，项目不存在'
    task_must_be_mulite_case_recommend = 100192, "推荐用例必须是多个才能执行"
    db_para_error = 100193, '创建db参数异常'
    db_name_rep = 100194, 'db名称重复'
    db_cr_error = 100195, '创建db异常'
    dbfac_para_error = 100196, '创建dbfac参数异常'
    dbfac_name_rep = 100197, 'dbfac名称重复'
    dbfac_cr_error = 100198, '创建dbfac异常'
    db_search_error = 100199, '查询db异常'
    db_edit_error = 100200, '编辑db异常'
    dbfac_search_error = 100201, '查询dbfac异常'
    dbfac_edit_error = 100202, '编辑dbfac异常'
    env_para_error = 100203, '创建环境参数异常'
    env_cr_error = 100204, '创建环境异常'
    env_search_error = 100205, '查询项目环境异常'
    env_edit_error = 100206, '编辑项目环境异常'
    model_para_error = 100207, '创建模块参数异常'
    add_assert_erro = 100208, '添加断言异常'
    get_assert_error = 100209, '获取断言异常'
    edit_assert_error = 100210, '编辑断言异常'
    add_pre_case_error = 100211, '添加前置用例异常'
    assert_fail = 100212, '断言失败'
    update_pre_case_error = 100213, '更新前置用例异常'
    get_case_detail_error = 100214, '获取用例详情异常'
