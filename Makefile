pdf : parallel_sn_sweeps_on_adapted_meshes.tex
	pdflatex parallel_sn_sweeps_on_adapted_meshes
	bibtex parallel_sn_sweeps_on_adapted_meshes
	pdflatex parallel_sn_sweeps_on_adapted_meshes
	pdflatex parallel_sn_sweeps_on_adapted_meshes

.PHONY : clean

clean :
	-rm parallel_sn_sweep_on_adapted_meshes.pdf
	-rm *.log *.aux *.bbl *.blg

