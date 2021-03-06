from CovidInfo_D import *
from pobocky import *
from Detail_D import *
from Detail_C import *
from DetskeKluby_D import *
from dovolena_D import *
from FM_D import *
from fulltext_C import *
from groupsearch_D import *
from HP_D import *
from LM_D import *
from poznavacky import *
from SDO_D import *
from SRL_C import *
from SRL_D import *
from HP_C import *
import HtmlTestRunner
#import HTMLTestRunner      ##at office PC gotta be set up like that (???)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCovidInfo_D('test_covidInfo_D'))
    suite.addTest(TestDetailHotelu_D("test_detail_D"))
    suite.addTest(TestDetailHotelu_C("test_detail_fotka"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_meal"))
    suite.addTest(TestDetailHotelu_C("test_detail_terminy_filtr_airport"))
    suite.addTest(TestDetskeKluby_D("test_kluby_D"))
    suite.addTest(TestDovolena_D("test_dovolena_D"))
    suite.addTest(TestFMexotika_D("test_FM_exotika_D"))
    suite.addTest(Test_Fulltext_C("test_fulltext_naseptavac"))
    suite.addTest(Test_Fulltext_C("test_fulltext_results_status_check"))
    suite.addTest(Test_Groupsearch_D("test_groupsearch_D"))
    suite.addTest(TestHP_D("test_homePage_D"))
    suite.addTest(TestLM_D("test_lM_isDisplayed"))
    suite.addTest(TestPobocky_D('test_pobocky_D'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_okruzni_D'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_vikendy_D'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_rodiny_D'))
    suite.addTest(TestPoznavacky_D('test_poznavacky_zazitky_D'))
    suite.addTest(TestSDO_D('test_SDO_D'))
    suite.addTest(Test_SRL_C('test_SRL_sort_cheapest'))
    suite.addTest(Test_SRL_C('test_SRL_sort_expensive'))
    suite.addTest(Test_SRL_C('test_SRL_map'))
    suite.addTest(Test_SRL_C('test_SRL_filtr_strava'))
    suite.addTest(Test_SRL_C('test_srl_C'))
    suite.addTest(TestSRL_D('test_SRL_D'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_SRL'))
    suite.addTest(Test_HP_C('test_HP_zlutak_to_groupsearch'))
    suite.addTest(Test_HP_C('test_HP_nejlepsi_nabidky_vypis_btn_switch'))
    suite.addTest(Test_HP_C('test_HP_slider_click_detail_hotelu'))
    return suite

def suite2():
    suite = unittest.TestSuite()
    suite.addTest(TestCovidInfo_D('test_covidInfo_D'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    #outfile = open("C:\Users\KDK\Desktop\HTML_TEST_REPORTS\sest_results.html", "w")
    outfile = open("results.html", "w")

    runner = HtmlTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title='FISCHER WEB Suite Report', report_name='FISCHER WEB Suite Report',
                            open_in_browser=True, description="FISCHER WEB Suite Report")
    #runner = HTMLTestRunner.HTMLTestRunner(log=True, verbosity=2, output='report', title='FISCHER WEB Suite Report', report_name='FISCHER WEB Suite Report', open_in_browser=True, description="FISCHER WEB Suite Report")
    ##at office PC gotta be set up like that (???)
    runner.run(suite())