all: run

run:
	nextflow run main.nf -resume -without-docker

run-fresh:
	nextflow run main.nf -without-docker

run-docker:
	nextflow run main.nf -with-docker

refresh-dag-image:
	rm -f flowchart.png
	nextflow run main.nf -with-dag flowchart.png

clean:
	rm -rf work results/*
