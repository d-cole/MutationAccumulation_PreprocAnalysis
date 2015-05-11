Running autoStampy.sh -DRAFT-

autoStampy maps sequence data using stampy for all data in a specific folder.
REQUIREMENTS:
	.SEQ.sample1_R2.fastq.gz
        HI.SEQ.sample1_R2.fastq.gz- Reference folder containing:
		For a reference genome file <genomeref>
		- <genomeref>.fa
			
		- <genomeref>.sthash

		- <genomeref>.stidx

		- <genomeref>.dict


How to run autoStampy:

	In the directory containing autoStampy type:
		./autoStampy.sh

	You will be propted for the following information:

		Enter directory containing sequence files (ex. /raw_reads/): 
			Enter the location of the directory that contains the .fastq.gz files. 
			Stampy will be launched for every file in this directory! 		
			Make sure to include the last "/" in the path specification.
				all_raw_reads/GP2-3ABCD <-- WILL NOT WORK
				all_raw_reads/GP2-3ABCD/ <-- GOOD

		Enter location of reference: (ex. /reference/pseudo_plastids)
			Enter the location of your reference files, ignoring the extensions. Stampy will determing which file to use based on the extensions.
		
		Enter output directory: (ex. /all_stampy_out/CC3-3A-H/)
			Make sure to include the last "/"!

Example:
Where raw_reads/sample1-3 contains:
	HI.SEQ.sample1_R1.fastq.gz          HI.SEQ.sample1_R2.fastq.gz
        HI.SEQ.sample2_R1.fastq.gz          HI.SEQ.sample2_R2.fastq.gz
        HI.SEQ.sample3_R1.fastq.gz          HI.SEQ.sample3_R2.fastq.gz


$ ./autoStampy.sh
Enter directory containing sequence files (ex. /raw_reads/): 
raw_reads/sample1-3/
Enter location of reference: (ex. /reference/pseudo_plastids)
reference/mGenome 
Enter output directory: (ex. /all_stampy_out/CC3-3A-H/)
stampy_out/

This will make the following call for every sample in the raw_reads folder
	/data/wei.wang/stampy-1.0.23/stampy.py -t 6 \ 
		-g reference/mGenome \ 
		-h reference/mGenome \ 
		-M  HI.SEQ.sample1_R1.fastq.gz\ 
		HI.SEQ.sample1_R2.fastq.gz >\ 
		stampy_out/sample1.sam \ 
		2>stampy_out/sample1.err &

	In this case, the command will be executed for Samples(1-3).

 
	
