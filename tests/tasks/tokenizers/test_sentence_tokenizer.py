# -*- coding: utf-8 -*-
from . import SentenceTokenizerTask
import unittest
import os

class SentenceTokenizerTaskTestCase(unittest.TestCase):
    task = None
    currentDirectory = "%s" % (os.path.dirname(os.path.realpath(__file__)), )
    directory = "%s/../../data/text/" % (currentDirectory,)

    name = "Sentence Tokenizer Task"

    def setUp(self):
        self.task = SentenceTokenizerTask(name="Sentence Tokenizer task")

    def tearDown(self):
        self.task = None

    def test_task_initialization_fails_if_name_is_None(self):
        """
        Test that a Sentence Tokenizer Task task throws an exception if the name is None
        """
        self.assertRaises(Exception, SentenceTokenizerTask, None)

    def test_task_initialization_fails_if_name_is_empty(self):
        """
        Test that a Sentence Tokenizer Task task throws an exception if the name is Empty
        """
        self.assertRaises(Exception, SentenceTokenizerTask, "")

    def test_task_initialization(self):
        """
        Test that a Sentence Tokenizer Task task is not None
        """
        self.assertIsNotNone(self.task)


    def test_task_tokenize_text(self):
        """
        Test the this task is tokenizing the text correctly
        """
        text = self.helper_readFilename('en/article1.txt')
        input = {"data":text}

        expected = {'data': [u'Congress\u2019s national security leadership is facing its biggest shakeup in years as some of its longest - serving and most influential members retire, seek other offices or risk losing their seats in tough reelections.', u'The potential brain drain on key House and Senate oversight panels, mostly among GOP lawmakers like Sen. John Mc.', u'Cain (R - Ariz. ) , comes as conflicts in hot spots like Iraq, Syria and Afghanistan and a series of terrorist attacks heighten worries about threats from abroad.', u'It\u2019s also happening at a time when one of the biggest anxieties about Republican standard - bearer Donald Trump is his lack of experience in national defense.', u'Story Continued Below.', u'The sweep, which would also impact some prominent Democrats, is already underway with the surprising primary loss Tuesday of Rep. Randy Forbes of Virginia, one of the highest - ranking Republicans on the Armed Services Committee.', u'But perhaps over a dozen key lawmakers could be gone by the time a new president is sworn in January \u2014 including Mc.', u'Cain and his hawkish ally Sen. Kelly Ayotte (R - N. H. ) , who are both fighting for their political lives, as well as nine members on the influential House panel who have decided to run for the Senate or retire.', u'The turnover could be the highest since the 2010 midterm elections, when four House Armed Services lawmakers retired or ran for other offices and 11 were defeated in their bids for reelection.', u'In that election, Republicans regained a majority in the House while the Senate ranks were thinned amid multiple retirements and the deaths of two congressional heavyweights, Democrats Robert Byrd and Ted Kennedy.', u'"There is a lot of turnover," said House Armed Services Chairman Mac Thornberry (R - Texas) , who was first elected in 1994.', u'"And I do get concerned how few people are still here who were here on 9/11 and remember that that can happen, out of the blue on a clear day.', u'"The practical result of the churn, defense experts say, is a loss of institutional knowledge on the committees responsible for crafting nearly the only legislation that reliably passes Congress each year: the National Defense Authorization Act.', u'It also raises questions about how those defense committees, with newly minted rank - and - file members replacing some seasoned legislators, will conduct oversight and negotiate with the new administration and Pentagon leadership.', u'"The sad truth is that Congress has already hemorrhaged generations\u2019 worth of national security thought leaders and party stalwarts who could shape the big debates, conduct robust oversight of the Pentagon and generate meaningful legislation and policy changes that transcend home districts or interests," said Mackenzie Eaglen, a defense analyst at the conservative - leaning American Enterprise Institute.', u'Indeed, the tenure of an average Senate Armed Services member has plummeted from eleven and a half years of service in the chamber in 2009 to six and a half years, according to a POLITICO analysis of the committee rosters.', u'The shift reflects the loss of a slew of congressional heavyweights on the panel, including former chairman Carl Levin (D - Mich. ) , Independent Sen. Joe Lieberman of Connecticut, and Kennedy and Byrd \u2014 who died in office in 2009 and 2010, respectively.', u'The congressional tenure of an average member of the House Armed Service Committee, meanwhile, is seven years as of 2015, about the same as 2009, though that level of institutional experience on the committee rose after falling to just over six years in each of the last two congresses.', u'Forbes, who lost his primary Tuesday in a reconfigured district, is the most high profile national security departure so far this election season.', u"The Virginian is the third most - senior House Armed Services Republican, and as chairman of the Seapower Subcommittee has been a critic of the Obama administration's shipbuilding plans, arguing instead for a major buildup to a 350-ship Navy.", u"Another House Republican, Rep. Joe Heck of Nevada, who as chair of the personnel subcommittee helped craft overhauls of the military's retirement and health systems as chairman of the personnel subcommittee, but has elected to pursue the Senate seat being vacated by Minority Leader Harry Reid.", u"The panel's second - ranking Democrat, Loretta Sanchez of California, is also giving up her spot on the committee to run for the Senate.", u'Other retirees include Reps. Jeff Miller of Florida and John Kline of Minnesota \u2014 the fourth and ninth most senior Armed Services Republicans \u2014 as well as Rep. Chris Gibson (R - N. Y. )', u", the architect of the committee's plan to halt the drawdown in size of the Army and Marine Corps.", u'"I think it\'s too early to make a firm call, but the HASC could lose a great deal of expertise on both sides of the aisle," said Justin Johnson, a former aide to multiple House Armed Services Republicans who is now with the Heritage Foundation.', u'And while no members of the Senate Armed Services Committee are retiring this year, two prominent Republicans on the committee \u2014 chairman Mc.', u'Cain and Ayotte \u2014 face tough reelection battles.', u"Ayotte, who chairs the panel's Readiness Subcommittee, has most notably been a vocal critic of the White House's push to close the terrorist detention center at Guantanamo Bay, Cuba.", u'First elected in 2010, the New Hampshire Republican has argued the Obama administration is rushing to empty the prison and authored provisions in the NDAA to slow the transfers.', u'Mc.', u"Cain, meanwhile, has used his two years wielding the Senate Armed Services gavel to push controversial changes to the Pentagon's bureaucracy, particularly the department's weapons acquisitions process.", u'Should he lose reelection, Heritage\'s Johnson noted that the next Republican in line, Oklahoma Sen. Jim Inhofe, "certainly has different priorities" from Mc.', u'Cain.', u'Eaglen argued that, over time, Senate turnover has a deeper impact.', u'"Since it is the more deliberative body, it has the time .', u'and staff and resources to take a longer view on major change," Eaglen said.', u'"The Senate typically provides continuity across Congresses to carry over undone work and take the time to get it right.', u'"Mieke Eoyang, a former House Armed Services staffer and Kennedy aide now with Third Way, said the turnover results in members who advance in seniority without learning "the practice of moving issues forward.', u'""It certainly will be a loss of process knowledge," Eoyang said.', u'And while the turnover from the past several election cycles has reduced the number of seasoned legislators on the committee, what matters, lawmakers and experts say, is who replaces those departing members.', u'"The good news is that the HASC has a lot of rising national security stars, both at the mid and junior levels," Johnson added.', u'"These more junior members lack the legislative experience, but many of them have great national security perspectives.', u'""It\'s the nature of life, in all aspects of it," House Armed Services ranking Democrat Adam Smith said of the churn.', u'"And I think we have plenty of capable members further down the rows there that are going to fill those gaps quite nicely.', u'"The Washington state Democrat and Thornberry said junior and mid - level members have already taken leadership roles on certain issues.', u'That talent, Smith said, includes Democrats Marc Veasey of Texas and Seth Moulton of Massachusetts as well as Republicans Martha Mc.', u'Sally of Arizona and Jackie Walorski of Indiana.', u"Newer members, Thornberry argued, have also brought outside experience that has proved helpful to the committee, even if it's not legislative experience.", u'"So you lose some of the institutional \'how Congress works,\' but you\'ve also picked up members with operational experience as a Marine on the ground in Iraq or a pilot over Afghanistan," Thornberry said.', u'"And that adds a lot too.', u'So it\'s not all a negative," he added.\n']}
        actual = self.task.execute(input)
        print(actual)

        self.assertEqual(expected, actual)



    def helper_readFilename(self, filename=''):
        if not filename:
            raise Exception("The file is empty")

        fileToRead = "%s%s" % (self.directory, filename)

        f = open(fileToRead, 'r')
        text = f.read()
        f.close()

        return text
