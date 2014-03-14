#! /usr/bin/env python
# autogenerated from sate_ui.xml by generate_ui.py

from pasta.usersettingclasses import ChoiceUserSetting, UserSettingsContainer, UserSettingGroup
from pasta.usersettingclasses import FloatUserSetting, StringUserSetting, IntUserSetting, BoolUserSetting

class PastaUserSettings(UserSettingsContainer):
    def __init__(self):
        UserSettingsContainer.__init__(self)
        self.faketree = UserSettingGroup('faketree')
        self._categories.append('faketree')
        self.raxml = UserSettingGroup('raxml')
        self._categories.append('raxml')
        self.randtree = UserSettingGroup('randtree')
        self._categories.append('randtree')
        self.opal = UserSettingGroup('opal')
        self._categories.append('opal')
        self.fakealigner = UserSettingGroup('fakealigner')
        self._categories.append('fakealigner')
        self.fasttree = UserSettingGroup('fasttree')
        self._categories.append('fasttree')
        self.muscle = UserSettingGroup('muscle')
        self._categories.append('muscle')
        self.sate = UserSettingGroup('sate')
        self._categories.append('sate')
        self.probalign = UserSettingGroup('probalign')
        self._categories.append('probalign')
        self.padaligner = UserSettingGroup('padaligner')
        self._categories.append('padaligner')
        self.clustalw2 = UserSettingGroup('clustalw2')
        self._categories.append('clustalw2')
        self.mafft = UserSettingGroup('mafft')
        self._categories.append('mafft')
        self.hmmeralign = UserSettingGroup('hmmeralign')
        self._categories.append('hmmeralign')
        self.commandline = UserSettingGroup('commandline')
        self._categories.append('commandline')
        self.prank = UserSettingGroup('prank')
        self._categories.append('prank')
        self.mafft.add_option('path', StringUserSetting(name='path', default='', short_name=None, help='Path to MAFFT executables', subcategory=None))
        self.hmmeralign.add_option('path', StringUserSetting(name='path', default='', short_name=None, help='Path to hmmeralign script', subcategory=None))
        self.padaligner.add_option('path', StringUserSetting(name='path', default='', short_name=None, help='Path to pad_aligner.py executables', subcategory=None))
        self.fakealigner.add_option('path', StringUserSetting(name='path', default='', short_name=None, help='Path to fakealigner file (can be empty)', subcategory=None))
        self.faketree.add_option('path', StringUserSetting(name='path', default='', short_name=None, help='Path to faketree file (can be empty)', subcategory=None))
        self.randtree.add_option('path', StringUserSetting(name='path', default='', short_name=None, help='Path to randtree executable', subcategory=None))
        self.prank.add_option('path', StringUserSetting(name='path', default='', short_name=None, help='Path to PRANK executable', subcategory=None))
        self.randtree.add_option('path', StringUserSetting(name='path', default='', short_name=None, help='Path to randtree executables', subcategory=None))
        self.raxml.add_option('path', StringUserSetting(name='path', default='', short_name=None, help='Path to RAxML', subcategory=None))
        self.raxml.add_option('model', StringUserSetting(name='model', default='', short_name=None, help='Substitution model used by RAxML. [GTRCAT for dna and PROTCATWAGF for aa]', subcategory=None))
        self.raxml.add_option('args', StringUserSetting(name='args', default='', short_name=None, help='Arguments to be passed to RAxML.', subcategory=None))
        self.fasttree.add_option('path', StringUserSetting(name='path', default='', short_name=None, help='Path to FastTree', subcategory=None))
        self.fasttree.add_option('model', StringUserSetting(name='model', default='', short_name=None, help='Substitution model used by FastTree. [-gtr for dna and -wag -gamma (WAG) for aa]', subcategory=None))
        self.fasttree.add_option('options', StringUserSetting(name='options', default='', short_name=None, help='Options to be passed to FastTree (equivalent of args).', subcategory=None))
        self.fasttree.add_option('args', StringUserSetting(name='args', default='', short_name=None, help='Arguments to be passed to FastTree.', subcategory=None))
        self.opal.add_option('path', StringUserSetting(name='path', default='', short_name=None, help='Path to Opal jar file', subcategory=None))
        self.clustalw2.add_option('path', StringUserSetting(name='path', default='', short_name=None, help='Path to clustalw2 exeutable', subcategory=None))
        self.muscle.add_option('path', StringUserSetting(name='path', default='', short_name=None, help='Path to muscle exeutable', subcategory=None))
        self.probalign.add_option('path', StringUserSetting(name='path', default='', short_name=None, help='Path to ProbalignAligner exeutable', subcategory=None))
        self.commandline.add_option('exportconfig', StringUserSetting(name='exportconfig', default=None, short_name=None, help='Export the configuration to the specified file and exit. This is useful if you want to combine several configurations and command line settings into a single configuration file to be used in other analyses.', subcategory=None))
        self.commandline.add_option('input', StringUserSetting(name='input', default=None, short_name='i', help='input sequence file', subcategory=None))
        self.commandline.add_option('treefile', StringUserSetting(name='treefile', default=None, short_name='t', help='starting tree file', subcategory=None))
        self.commandline.add_option('temporaries', StringUserSetting(name='temporaries', default=None, short_name=None, help="directory that will be the parent for this job's temporary file [default in PASTA home]", subcategory=None))
        self.commandline.add_option('job', StringUserSetting(name='job', default='pastajob', short_name='j', help='job name [pastajob]', subcategory=None))
        self.commandline.add_option('timesfile', StringUserSetting(name='timesfile', default=None, short_name=None, help='optional file that will store the times of events during the PASTA run. If the file exists, new lines will be', subcategory=None))
        self.commandline.add_option('aligned', BoolUserSetting(name='aligned', default='False', short_name='a', help='If used, then the input file be will treated as aligned for the purposes of the first round of tree inference (the algorithm will start with tree searching on the input before re-aligning). This option only applies if a starting tree is NOT given.', subcategory=None))
        self.commandline.add_option('raxml_search_after', BoolUserSetting(name='raxml_search_after', default='False', short_name=None, help='If used, the the completion of the PASTA algorithm will be followed by a tree search using RAxML. This can be useful if a very fast and approximate tree estimator is used during the PASTA algorithm. [default: disabled]', subcategory=None))
        self.commandline.add_option('two_phase', BoolUserSetting(name='two_phase', default='False', short_name=None, help='If used, then the program will not perform the PASTA algorithm. Instead it will simply call the sequence aligner to align the entire dataset then will call the tree estimator to obtain the tree.', subcategory=None))
        self.commandline.add_option('untrusted', BoolUserSetting(name='untrusted', default='False', short_name=None, help='If used, then the data in the input file will be parsed using a more careful procedure. This will generate more helpful error messages, but will use more memory and be much slower for large inputs. If this option is omitted, the error messages resulting from invalid input data will be more cryptic.', subcategory=None))
        self.commandline.add_option('datatype', ChoiceUserSetting(name='datatype', default='DNA', choices=['DNA', 'RNA', 'Protein'], multiple_choices=False, short_name='d', help='Specify DNA, RNA, or Protein to indicate what type of data is specified. Note that this option is NOT automatically determined [default: dna]', subcategory=None))
        self.commandline.add_option('keeptemp', BoolUserSetting(name='keeptemp', default='False', short_name='k', help='Keep temporary running files? [default: disabled]', subcategory=None))
        self.commandline.add_option('keepalignmenttemps', BoolUserSetting(name='keepalignmenttemps', default='False', short_name=None, help='Keep even the realignment temporary running files (this only has an effect if keeptemp is also selected).', subcategory=None))
        self.commandline.add_option('multilocus', BoolUserSetting(name='multilocus', default='False', short_name='m', help='Analyze multi-locus data? NOT SUPPORTED IN CURRENT PASTA version.', subcategory=None))
        self.commandline.add_option('missing', ChoiceUserSetting(name='missing', default=None, choices=['Ambiguous', 'Absent'], multiple_choices=False, short_name=None, help='How to deal with missing data symbols. Specify either "Ambiguous" or "Absent" if the input data contains ?-symbols', subcategory=None))
        self.commandline.add_option('auto', BoolUserSetting(name='auto', default='False', short_name=None, help='This option is mostly for backward compatibility. If used, then automatically identified default values for the max_subproblem_size, number of cpus, tools, breaking strategy, masking criteria, and stopping criteria will be used. This is just like using the default options. However, [WARNING] when auto option is used PASTA overrides the value of these options even if you have supplied them; we recommend that you run this option with --exportconfig to see the exact set of options that will be used in your analysis.', subcategory=None))
        self.sate.add_option('num_cpus', IntUserSetting(name='num_cpus', default=1, min=1, max=None, short_name=None, help='The number of processing cores that you would like to assign to PASTA.  This number should not exceed the number of cores on your machine. [default: number of cores available on the machine]', subcategory='platform'))
        self.sate.add_option('max_mem_mb', IntUserSetting(name='max_mem_mb', default=1024, min=256, max=None, short_name=None, help='The maximum memory available to OPAL (for the Java heap size when running Java tools).', subcategory='platform'))
        self.sate.add_option('aligner', StringUserSetting(name='aligner', default='mafft', short_name=None, help='The name of the alignment program to use for subproblems. [default: mafft]', subcategory='tools'))
        self.sate.add_option('merger', StringUserSetting(name='merger', default='opal', short_name=None, help='The name of the alignment program to use to merge subproblems. [default: OPAL for dna, muscle for AA]', subcategory='tools'))
        self.sate.add_option('tree_estimator', StringUserSetting(name='tree_estimator', default='fasttree', short_name=None, help='The name of the tree inference program to use to find trees on fixed alignments. [default: fasttree]', subcategory='tools'))
        self.sate.add_option('break_strategy', ChoiceUserSetting(name='break_strategy', default='centroid', choices=['centroid', 'longest'], multiple_choices=True, short_name=None, help='The method for choosing an edge when bisecting the tree during decomposition [default: centroid]', subcategory='decomposition'))
        self.sate.add_option('max_subproblem_size', IntUserSetting(name='max_subproblem_size', default=3, min=0, max=None, short_name=None, help='The maximum size (number of leaves) of subproblems.  When a subproblem contains this number of leaves (or fewer), then it will not be decomposed further. [default: automatically picked based on alignment size]', subcategory='decomposition'))
        self.sate.add_option('max_subproblem_frac', FloatUserSetting(name='max_subproblem_frac', default=0.5, min=0.0, max=None, short_name=None, help='The maximum size (number of leaves) of subproblems specified in terms as a proportion of the total number of leaves.  When a subproblem contains this number of leaves (or fewer), then it will not be decomposed further. [default: automatically picked based on alignment size]', subcategory='decomposition'))
        self.sate.add_option('start_tree_search_from_current', BoolUserSetting(name='start_tree_search_from_current', default='False', short_name=None, help='If selected that the tree from the previous iteration will be given to the tree searching tool as a starting tree.', subcategory='searching'))
        self.sate.add_option('move_to_blind_on_worse_score', BoolUserSetting(name='move_to_blind_on_worse_score', default='False', short_name=None, help='If True then PASTA will move to the blind mode as soon it encounters a tree/alignment pair with a worse score. This is essentially the same as running in blind mode from the beginning, but it does allow one to terminate a run at an interval from the first time the algorithm fails to improve the score.', subcategory='acceptance'))
        self.sate.add_option('blind_mode_is_final', BoolUserSetting(name='blind_mode_is_final', default='True', short_name=None, help='When the blind mode is final, then PASTA will never leave blind mode once it is has entered blind mode.', subcategory='acceptance'))
        self.sate.add_option('blind_after_total_time', FloatUserSetting(name='blind_after_total_time', default=-1.0, min=None, max=None, short_name=None, help='Maximum time (in seconds) that PASTA will run before switching to blind mode. [default: disabled]', subcategory='acceptance'))
        self.sate.add_option('blind_after_total_iter', IntUserSetting(name='blind_after_total_iter', default=0, min=None, max=None, short_name=None, help='Maximum number of iterations that PASTA will run before switching to blind mode. [default: 0]', subcategory='acceptance'))
        self.sate.add_option('blind_after_time_without_imp', FloatUserSetting(name='blind_after_time_without_imp', default=-1.0, min=None, max=None, short_name=None, help='Maximum time (in seconds) that PASTA will run without an improvement in likelihood score before switching to blind mode. [default: disabled]', subcategory='acceptance'))
        self.sate.add_option('blind_after_iter_without_imp', IntUserSetting(name='blind_after_iter_without_imp', default=-1, min=None, max=None, short_name=None, help='Maximum number of iterations without an improvement in likelihood score that PASTA will run before switching to blind mode. [default: disabled]', subcategory='acceptance'))
        self.sate.add_option('time_limit', FloatUserSetting(name='time_limit', default=86400.0, min=None, max=None, short_name=None, help='Maximum time (in seconds) that PASTA will continue starting new iterations of realigning and tree searching. If the number is less than 0, then no time limit will be used. [default: disabled]', subcategory='termination'))
        self.sate.add_option('iter_limit', IntUserSetting(name='iter_limit', default=-1, min=None, max=None, short_name=None, help='The maximum number of iteration that the PASTA algorithm will run.  If the number is less than 1, then no iteration limit will be used. [default: 3]', subcategory='termination'))
        self.sate.add_option('after_blind_time_term_limit', FloatUserSetting(name='after_blind_time_term_limit', default=-1.0, min=None, max=None, short_name=None, help='Maximum time (in seconds) that PASTA will continue starting new iterations of realigning and tree searching after PASTA has entered blind mode. If the number is less than 0, then no time limit will be used. [default: disabled]', subcategory='termination'))
        self.sate.add_option('after_blind_iter_term_limit', IntUserSetting(name='after_blind_iter_term_limit', default=-1, min=None, max=None, short_name=None, help='The maximum number of iteration that the PASTA algorithm will run after PASTA has entered blind mode.  If the number is less than 1, then no iteration limit will be used. [default: disabled]', subcategory='termination'))
        self.sate.add_option('time_without_imp_limit', FloatUserSetting(name='time_without_imp_limit', default=-1.0, min=None, max=None, short_name=None, help='Maximum time (in seconds) since the last improvement in score that PASTA will continue starting new iterations of realigning and tree searching. If the number is less than 0, then no time limit will be used. [default: disabled]', subcategory='termination'))
        self.sate.add_option('iter_without_imp_limit', IntUserSetting(name='iter_without_imp_limit', default=-1, min=None, max=None, short_name=None, help='The maximum number of iterations without an improvement in score that the PASTA algorithm will run.  If the number is less than 1, then no iteration limit will be used. [default: disabled]', subcategory='termination'))
        self.sate.add_option('after_blind_time_without_imp_limit', FloatUserSetting(name='after_blind_time_without_imp_limit', default=-1.0, min=None, max=None, short_name=None, help='Maximum time (in seconds) since the last improvement in score that PASTA will continue starting new iterations of realigning and tree searching after entering BLIND mode. If the number is less than 0, then no time limit will be used. [default: disabled]', subcategory='termination'))
        self.sate.add_option('after_blind_iter_without_imp_limit', IntUserSetting(name='after_blind_iter_without_imp_limit', default=1, min=None, max=None, short_name=None, help='The maximum number of iterations without an improvement in score that the PASTA algorithm will run after entering BLIND mode.  If the number is less than 1, then no iteration limit will be used. [default: disabled]', subcategory='termination'))
        self.sate.add_option('output_directory', StringUserSetting(name='output_directory', default=None, short_name='o', help='directory for output files (defaults to input file directory)', subcategory='output'))
        self.sate.add_option('return_final_tree_and_alignment', BoolUserSetting(name='return_final_tree_and_alignment', default='True', short_name=None, help='Return the best likelihood tree and alignment pair instead of those from the last iteration; this is discouraged with masking option enabled.', subcategory='output'))
        self.sate.add_option('mask_gappy_sites', IntUserSetting(name='mask_gappy_sites', default=1, min=0, max=None, short_name=None, help='The minimum number of non-gap characters required in each column passed to the tree estimation step. Columns with fewer non-gap characters than the given threshold will be masked out before passing the alignment into the tree estimation module. These columns will be present in the final alignment. [default: 0.1% of alignment size]', subcategory='searching'))
