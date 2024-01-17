# -*- coding: utf-8 -*-

import os
import threading
import buter

from Exp.ecolony.E_Colony_Database_configuration_information_leakage import ecdcil
from Exp.ecolony.E_cology_OA_Beanshellassembly_rce import *
from Exp.ecolony.E_Colony_OA_WorkflowCenterTreeData_interface_SQL_injection import ecwtsqli
from Exp.ecolony.E_Cology_V8_FrontDesk_Sql import ecv8sql
from Exp.ecolony.E_CologyCloud_Bridge_Arbitrary_File_Reading import eccbafr
from Exp.ecolony.ecology_oa_FileDownloadForOutDoc_sql import ecfrsqli
from Exp.ecolony.E_cology_uploadify_fileup_RCE import eofu9fileup
from Exp.ecolony.E_cology_mobile_upload_save_fileup_RCE import ecmusfileup

from Exp.Dahua.Dahua_Smart_Park_Arbitrary_Pwd_Read import dhapread
from Exp.Dahua.Dahua_Smart_Park_Comprehensive_Management_Platform_fileup_RCE import dhspcmpfileup
from Exp.Dahua.Dahua_Smart_Park_Comprehensive_Management_Platform_searchJson_SQL import dhspcmpsSQL

from Exp.seeyou.seeyou_OA_wpsassistservlet_fileip_RCE import sywfileip
from Exp.seeyou.seeyou_administrator_login_fileupRCE import syaloginfileip

#用友
from Exp.yonyou.yonyou_grp_u8_information_disclosure import syguxxl
from Exp.yonyou.yonyouGRP_U8AppProxy_fileup_RCE import yyu8fileuprce
from Exp.yonyou.yonyouU8C_fileuploadRCE import yyU8CuploadRCE
from Exp.yonyou.yonyou_chanjet_RCE import yychanjetRCE
from Exp.yonyou.yonyouNC_Cloud_uploadChunk import yyncuploadchunk
from Exp.yonyou.yonyou_crm_anyfileread import yycrmanyfileread

from Exp.HIKVISION.hkvs_Comprehensive_Security_Management_Platform_Env_Information_Leakage import hkenvil
from Exp.HIKVISION.hkvs_Video_encoding_device_access_gateway_showFile_arbitrary_filedown import hkvedagsfiledown
from Exp.HIKVISION.hkvs_Isecure_Center_RCE import hkicfileup
from Exp.HIKVISION.hkvs_gatway_anyfileRead import hkvsgatewayRead
from Exp.HIKVISION.hkvs_IP_NetworkRCE import hkvsIPRCE

from Exp.Kingdee.Kingdee_Cloud_Starry_Sky_CommonFileserver_Arbitrary_File_Read import kdcsscafileread
from Exp.Kingdee.Kingdee_EAS_dir_traversal import KingdeeEASdirtra
from Exp.Kingdee.kingdee_ScpSupRegHandler_uploadRCE import KingdeeScpSuRegHandler

from Exp.jinher.jinher_oa_unauthorized import jinherun
from Exp.jinher.jinher_oa_c6_GetSgIData_SQL_Inj_RCE import jhoac6gsiRCE

from Exp.kuboard.Kuboard_default_passwd import kdp

from Exp.Nacos.nacos_sync_unauthorized import nasyun

from Exp.kinpan.kinpan_getsysteminfo_unauthorized import kpgetinfoun

from Exp.sanliulin.New_Tianqing_Terminal_Security_Management_System_Information_Leakage import ntqinfoleak
from Exp.sanliulin.SecGate_3600_firewall_obj_app_upfile import SG3600fileupRCE
from Exp.sanliulin.SecGate_firewall_UserAccount_Leakage import SecGateuserLeakage

from Exp.anheng.Anheng_Mingyu_Security_Gateway_aaa_Submit_RCE import ahmyaaa

from Exp.flyrise.flyrise_magepath_filereads import flyrisefileread

from Exp.glodon.glodon_LinkworksOA_sql import gloasql

from Exp.showdoc.showdoc_fileup import sdfileup

from Exp.hand.hd_srm_login_bypass import hdsrmlb

from Exp.iOffice.iOffice_OA_sqlinject import ioffOAsql

from Exp.hongjing.hongjing_HCM_codesettree_SQL import hjhcmsql
from Exp.hongjing.hongjing_eHR_fileupload import hjfileup

from Exp.jinshan.Jinshan_Terminal_Security_System_Arbitrary_File_Upload import jstssafileup

from Exp.Landray.landray_oa_Any_file_read import lanoaanyfileread

from Exp.wanhu.wanhu_oa_controller_fileupload import whoafileup

from Exp.QiWang.QiWangERP import QiWangerpRCE

from Exp.EasyCVR.EasyCVR_xxxl import easycvrxxxl

#明源
from Exp.mingyuan.mingyuanERP_time_blind_sqlinjection import mingyuanSQL

#锐捷
from Exp.ruijie.ruijie_switch_EXCU_shell_pass_information_leakage import RJSWEXCUxxxl

#禅道
from Exp.ZenTao.ZenTao_16_5_SQL import ZTrouteSQL

#Nginx
from Exp.Nginx.nginx_webUI_RCE import nginxWebuiRCE

#时空智友
from Exp.sxskzy.skzy_login_allreadfile import skzyfileread
from Exp.sxskzy.skzy_fileuploadRCE import skzyfileup_RCE

#华测
from Exp.huace.huace_allfileread import HCfileread
from Exp.huace.huace_Config_xml_xxxl import HCConfigxxxl

#中远
from Exp.zhongyuan.zhongyuan_tokens_sql import zytokensSQL
from Exp.zhongyuan.zhonyuan_admin_sql import zyadminSQL
lock = threading.Lock()  # 为线程安全打印定义一个锁

#华夏
from Exp.huaxia.huaxia_erp_xxxl import huaxiaerpxxxl

#Nocodb
from Exp.NocoDB.nocodb_allfile_read import nocodballfileread

from Exp.eosine.eosine_wuliuUploadfile_RCE import eosineUploadRCE

from Exp.Enter.zheda_enter_fileupload_RCE import zhedaenterUPload
from Exp.Enter.enter_sql import enterSQL

from Exp.superdata.superdata_all_fileupload import sudafileupload

from Exp.DaTang.datang_rkl_Information_Leakage import datangrklinformation

from Exp.hongyun.hongyun_Cloud_platform_read import hysecCPread

from Exp.Ruoyi.ruoyi_fileread import ruoyifileread

from Exp.Yunanbao.yunanbao_config_fastjsonRCE import yabconfigRCE

from Exp.panabit.Panabit_panalog_sql import panabitlogsql

from Exp.huawei.huawei_Auth_fileread import hauweiauthreadfile

from Exp.idocv.idocv_anyfile_read import iDocView

from Exp.JeecgBoot.JeecgBoot_testConnectionRCE import jeecgRCE

from Exp.Tosei.Tosei_webRCE import toseiRCE

from Exp.Jieshun.jieshun_jielink_leak import jieshunleak

from Exp.eqccd.eqccd_oa_ajaxSQL import eqccdOASQL

from Exp.Other.liananyun_anyadduser import yiliantong
from Exp.Other.HWL_2511_SS_routeRCE import HWL2511SSRCE
from Exp.Other.OfficeWeb365_Indexs_anyfileread import office365Read

# 公用的模板
def process_urls(urls, max_threads, *functions):
    thread_list = []
    for url in urls:
        # 对于每个 URL，创建一组线程并启动
        threads = [threading.Thread(target=func, args=(url,)) for func in functions]
        for t in threads:
            t.start()
            thread_list.append(t)
            while len(thread_list) >= max_threads:
                time.sleep(0.5)
                thread_list = [t for t in thread_list if t.is_alive()]
    for t in thread_list:
        t.join()
files_path = "url.txt"
# 文件读取的方法
def read_urls_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        urls = [url.strip() for url in f.readlines()]
    return urls

# # 最大线程
# def get_max_threads(max_threads):
#     return max_threads


'''泛微'''
def fanwei():
    info = '''
    泛微数据库配置信息泄露
    泛微OA beanshell组件rce
    泛微OA WorkflowCenterTreeData接口SQL注入
    泛微V8 前台sql注入
    泛微云桥任意文件读取
    泛微OA FileDownloadForOutDoc reception sql注入
    泛微-office9文件上传
    泛微mobile文件上传
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,ecdcil,E_cology_OA_Beanshell1,E_cology_OA_Beanshell2,E_cology_OA_Beanshell3,E_cology_OA_Beanshell4,ecwtsqli,ecv8sql,eccbafr,ecfrsqli,eofu9fileup,ecmusfileup,)


# #用友
# def yonyou():
#     with open('url.txt', 'r', encoding='utf-8') as f:
#         urls = []
#         for url in f.readlines():
#             urls.append(url.strip())
#     max_threads = int(input('Please enter the number of threads :  '))
#     thread_list = []
#     for url in urls:
#         # 对于每个 URL，创建一组线程并启动
#         threads = [
#             threading.Thread(target=yyu8fileuprce, args=(url,)),  # 用友GRP-U8 U8AppProxy任意文件上传
#             threading.Thread(target=syguxxl, args=(url,)),  # 用友grp-u8信息泄露
#             threading.Thread(target=yyU8CuploadRCE,args=(url,)),
#         ]
#
#         for t in threads:
#             t.start()
#             thread_list.append(t)
#             '''thread_list.append(t) 是将线程对象 t 添加到名为 thread_list 的列表中。这样做的目的是跟踪所有启动的线程，以便后续统一管理和监控它们的状态。
#             在代码中，每次创建并启动一个新的线程时，都会通过 thread_list.append(t) 将该线程对象添加到 thread_list 列表中。这样，在后续的部分可以使用 thread_list 来追踪当前活动的线程数量，并控制线程的并发执行。'''
#             # 控制当前活动线程数不超过最大线程数
#             while len(thread_list) >= max_threads:
#                 '''我们使用 len(thread_list) 来获取当前活动线程数，并与最大线程数 max_threads 进行比较。当活动线程数达到最大线程数时，代码会暂停执行，
#                 等待其中某些线程结束，以保持并发线程数不超过设定值。通过对 thread_list 进行操作（检查是否存活），我们可以控制线程的并发度。
#                 总结来说，thread_list.append(t) 是将线程对象添加到列表中，以便追踪和管理线程的状态和数量。'''
#                 time.sleep(0.5)
#
#                 '''这段代码使用了一个循环遍历 thread_list 中的每个线程对象 t。对于每个线程，如果 t.is_alive() 为真（即线程还活着），
#                 则将其添加到新的列表 alive_threads 中。最后，将 thread_list 更新为仅包含尚未结束的活动线程。
#                 这种写法更加直观易懂，通过显式的循环和条件判断来筛选出活动的线程，并更新线程列表。'''
#                 thread_list = [t for t in thread_list if t.is_alive()]
#
#     for t in thread_list:
#         t.join()

'''用友'''
def yonyou():
    info = '''
    用友U8 文件上传
    用友U8 Cloud 文件上传
    用友grp-8 信息泄露
    用友畅捷通T+GetStoreWarehouseByStore_RCE
    用友NC-Cloud-uploadChunk任意文件上传
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,yyu8fileuprce,yyU8CuploadRCE,syguxxl,yychanjetRCE,yyncuploadchunk,yycrmanyfileread)

'''大华'''
def dahua():
    info = '''
    大华智慧园区任意密码读取
    大华智慧园区综合管理平台文件上传
    大华智慧园区综合管理平台 searchJson SQL注入漏洞
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,dhapread,dhspcmpfileup,dhspcmpsSQL)

'''致远'''
def seeyou():
    info = '''
    致远OA wpsAssistServlet 任意文件上传
    致远管理员任意登陆导致文件上传RCE
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,sywfileip,syaloginfileip)

'''海康威视'''
def hkvs():
    info = '''
    hkvs 综合安防管理平台env信息泄漏
    hkvs 视频编码设备接入网关showFile任意文件下载
    hkvs isecure_center综合安防管理平台存在任意文件上传
    hkvs 安全接入网关任意文件读取漏洞

    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,hkenvil,hkvedagsfiledown,hkicfileup,hkvsgatewayRead)
    # process_urls(read_urls_from_file(files_path),max_threads,hkvsIPRCE)

'''金蝶'''
def kingdee():
    info = '''
    金蝶云星空CommonFileserver任意文件读取
    金蝶EAS 系统目录遍历
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,kdcsscafileread,KingdeeEASdirtra,KingdeeScpSuRegHandler)

'''金和'''
def jinher():
    info = '''
    金和OA 未授权
    金和OA C6_GetSgIDataQL注入导致RCE
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,jinherun,jhoac6gsiRCE)

'''Kuboard'''
def Kuboard():
    info = '''
    Kuboard 默认口令
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,kdp)

'''Nacos'''
def Nacos():
    info = '''
    Nacos-sync 未授权
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,nasyun)

'''kinpan'''
def kinpan():
    info = '''
    金盘微信管理平台getsysteminfo未授权
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,kpgetinfoun)

'''360'''
def sanliulin():
    info = '''
    三六零新天擎终端安全管理系统信息泄露
    网神 SecGate 3600 防火墙任意文件上传漏洞
    网神防火墙用户登录账号泄露漏洞
    '''
    print(info)
    process_urls(read_urls_from_file(files_path), max_threads, ntqinfoleak, SG3600fileupRCE, SecGateuserLeakage)

'''安恒'''
def anheng():
    info = '''
    明御安全网关_aaa_portal_auth_local_submit_RCE
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,ahmyaaa)

'''飞企互联'''
def flyrises():
    info = '''
    飞企互联FE业务协作平台magePath参数文件读取
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,flyrisefileread)

'''广联达'''
def gld():
    info = '''
    广联达Linkworks办公OASQL注入
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,gloasql)

'''showdoc'''
def showdoc():
    info = '''
    showdoc文件上传
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,sdfileup)

'''汉得'''
def hand():
    info = '''
    汉得SRMtomcat登录绕过
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,hdsrmlb)

'''红帆'''
def ioffice():
    info = '''
    红帆OA sql注入
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,ioffOAsql)

'''宏景'''
def hongjing():
    info = '''
    宏景 HCM codesettree SQL注入
    宏景 eHR 文件上传
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,hjhcmsql,hjfileup)

'''金山'''
def jinshan():
    info = '''
    金山终端安全系统任意文件上传
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,jstssafileup)

'''蓝凌'''
def landray():
    info = '''
    蓝凌OA 任意文件读取
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,lanoaanyfileread)

'''万户'''
def wanhu():
    info = '''
    万户 OA controller 任意文件上传 RCE
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,whoafileup)

'''企望'''
def qiwang():
    info = '''
    企望 ERP RCE
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,QiWangerpRCE)

'''明源'''
def mingyuan():
    info = '''
    明源 sql时间盲注
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,mingyuanSQL)

'''锐捷'''
def ruijie():
    info = '''
    锐捷 交换机EXEU_shell密码信息泄露
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,RJSWEXCUxxxl)

'''禅道'''
def zentao():
    info = '''
    禅道 router sql注入
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,ZTrouteSQL)

'''nginx'''
def nginx():
    info = '''
    nginxWebUI前台远程命令执行
    '''
    print(info)
    process_urls(read_urls_from_file(files_path), max_threads, nginxWebuiRCE)

'''时空智友'''
def skzy():
    info = '''
    时空智友企业流程化管控系统_login_文件读取
    时空智友企业流程化管控系统文件上传
    '''
    # urls = read_urls_from_file()
    # max_threads = get_max_threads()
    print(info)
    process_urls(read_urls_from_file(files_path), max_threads, skzyfileread, skzyfileup_RCE)

'''华测'''
def huace():
    info = '''
    华测监测任意文件读取
    华测监测系统数据库泄露
    '''
    # urls = read_urls_from_file("url.txt")
    # max_threads = get_max_threads()
    print(info)
    process_urls(read_urls_from_file(files_path), max_threads, HCConfigxxxl, HCfileread)

'''中远'''
def zhongyuan():
    info = '''
    中远麒麟堡垒机tokens SQL注入
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,zytokensSQL,zyadminSQL)

'''华夏'''
def huaxia():
    info = '''
    华夏 ERP 信息泄露
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,huaxiaerpxxxl)

'''NocoDB'''
def NocoDB():
    info = '''
    NocoDB 任意文件读取
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,nocodballfileread)

'''易思'''
def Eosine():
    info = '''
    易思智能物流无人值守系统文件上传
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,eosineUploadRCE)

'''浙大恩特'''
def Enter():
    info = '''
    浙大恩特客户资源管理系统任意文件上传
    浙大恩特CRM-SQL注入
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,zhedaenterUPload,enterSQL)

'''速达'''
def Superdata():
    info = '''
    速达软件全系产品存在任意文件上传
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,sudafileupload)

'''大唐'''
def Datang():
    info = '''
    大唐电信AC管理平台弱口令登录及信息泄露
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,datangrklinformation)

'''鸿运'''
def Hongyun():
    info = '''
    鸿运主动安全监控云平台存在任意文件读取
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,hysecCPread)

'''若依'''
def Ruoyi():
    info = '''
    若依管理系统存在任意文件读取
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,ruoyifileread)

'''云安宝'''
def Yunanbao():
    info = '''
    云安宝-云匣子 config接口存在fastjson命令执行漏洞
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,yabconfigRCE)

'''派网'''
def panabit():
    info = '''
    Panabit日志系统SQL注入漏洞
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,panabitlogsql)

'''华为'''
def huaewi():
    info = '''
    Huawei Auth-HTTP Server 1.0 存在任意文件读取
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,hauweiauthreadfile)

'''iDocView'''
def iDoc():
    info = '''
    I Doc View在线文档预览系统存在任意文件读取漏洞
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,iDocView)

'''Jeecg'''
def Jeecg():
    info = '''
    JeecgBoot testConnection 远程命令执行
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,jeecgRCE)

'''EasyCVR'''
def EasyCVR():
    info = '''
    EasyCVR 视频管理平台存在用户信息泄露
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,easycvrxxxl)

'''Toset'''
def Tosei():
    info = '''
    Tosei 自助洗衣机 network_test.php RCE
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,toseiRCE)

'''捷顺'''
def Jieshun():
    info = '''
    捷顺 JieLink智能终端操作平台默认口令漏洞
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,jieshunleak)

'''Other'''
def Other():
    info = '''
    脸爱云一脸通智慧管理平台任意用户添加
    HWL-2511-SS路由器命令执行
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,yiliantong,HWL2511SSRCE,office365Read)
    # process_urls(read_urls_from_file(files_path),max_threads,office365Read)

'''全程云'''
def Eqccd():
    info = '''
    全程云OA ajax.ashx SQL注入漏洞
    '''
    print(info)
    process_urls(read_urls_from_file(files_path),max_threads,eqccdOASQL)



if __name__ == '__main__':
    if not os.path.exists("reps"):
        os.makedirs("reps")

    while True:

        function_list = [zhongyuan,
                         panabit,
                         EasyCVR,
                         Eqccd,
                         Superdata,
                         iDoc,
                         Other,
                         Jeecg,
                         Tosei,
                         Yunanbao,
                         Ruoyi,
                         Hongyun,
                         Datang,
                         Jieshun,
                         Enter,
                         Eosine,
                         NocoDB,
                         huaxia,
                         yonyou,
                         fanwei,
                         dahua,
                         seeyou,
                         hkvs,
                         kingdee,
                         jinher,
                         Kuboard,
                         Nacos,
                         kinpan,
                         sanliulin,
                         anheng,
                         flyrises,
                         gld,
                         showdoc,
                         hand,
                         ioffice,
                         hongjing,
                         jinshan,
                         landray,
                         wanhu,
                         qiwang,
                         mingyuan,
                         ruijie,
                         zentao,
                         nginx,
                         skzy,
                         huace]  # 包含函数的列表
        choice = input('Please choose the operation you want to perform >>>    ')
        max_threads = int(input('Please enter the number of threads  >>>    '))
        #用友
        if choice == 'all':
            for func in function_list:
                func()
        elif choice == 'zhongyuanall':
            zhongyuan()

        elif choice == 'yonyouall':
            yonyou()

        #泛微
        elif choice == 'fanweiall':
            fanwei()

        #大华
        elif choice == 'dahuaall':
            dahua()

        #致远
        elif choice =='seeyouall':
            seeyou()

        #海康威视
        elif choice == 'hkvsall':
            hkvs()

        #金蝶
        elif choice == 'kingdeeall':
            kingdee()

        #金和
        elif choice == 'jinherall':
            jinher()

        elif choice =='kuboardall':
            Kuboard()

        elif choice == 'nacosall':
            Nacos()

        #金盘
        elif choice == 'kinpanall':
            kinpan()

        #360
        elif choice == '360all':
            sanliulin()

        #安恒
        elif choice == 'anhengall':
            anheng()

        #飞联
        elif choice == 'feilianall':
            flyrises()

        #广联达
        elif choice == 'gldall':
            gld()

        elif choice == 'showdocall':
            showdoc()

        elif choice == 'handall':
            hand()

        elif choice == 'iofficeall':
            ioffice()

        elif choice == 'hongjingall':
            hongjing()

        elif choice == 'jinshanall':
            jinshan()

        elif choice == 'landrayall':
            landray()

        #万户
        elif choice == 'wanhuall':
            wanhu()
        #企望
        elif choice =='qiwangall':
            qiwang()

        #明源
        elif choice == 'mingyuanall':
            mingyuan()

        #锐捷
        elif choice == 'ruijieall':
            ruijie()
        #禅道
        elif choice == 'zentaoall':
            zentao()
        #nginx
        elif choice == 'nginxall':
            nginx()

        #时空智友
        elif choice == 'skzyall':
            skzy()

        #华测
        elif choice == 'huaceall':
            huace()

        #华夏
        elif choice == 'huaxiaall':
            huaxia()
        #NocoDB
        elif choice == 'nocodball':
            NocoDB()

        #易思
        elif choice == 'eosineall':
            Eosine()

        #浙大恩特
        elif choice == 'enterall':
            Enter()

        #速达
        elif choice == 'sudaall':
            Superdata()

        #大唐
        elif choice == 'datangall':
            Datang()

        #鸿运
        elif choice == 'hongyunall':
            Hongyun()

        #若依
        elif choice == 'ruoyiall':
            Ruoyi()

        #云安宝
        elif choice == 'yunanbaoall':
            Yunanbao()

        #派网
        elif choice == 'panabitall':
            panabit()

        #华为
        elif choice == 'huaweiall':
            huaewi()

        #IDoc
        elif choice == 'Idocall':
            iDoc()

        #Jeecg
        elif choice == 'Jeecgall':
            Jeecg()

        #EasyCVR
        elif choice == 'Easycvrall':
            EasyCVR()

        #Tosei
        elif choice == 'Toseiall':
            Tosei()

        #捷顺
        elif choice == "jieshunall":
            Jieshun()

        #Other
        elif choice == 'Otherall':
            Other()

        #Eqccd
        elif choice == 'Eqccdall':
            Eqccd()

        else:
            print(buter.colors.LAN + "未监测到有效输入,即刻退出" + buter.colors.END)
            break


