pdf : parallel_sweep_on_adapted_mesh.tex
	pdflatex parallel_sweep_on_adapted_mesh
	bibtex parallel_sweep_on_adapted_mesh
	pdflatex parallel_sweep_on_adapted_mesh
	pdflatex parallel_sweep_on_adapted_mesh

.PHONY : clean

clean :
	-rm parallel_sweep_on_adapted_mesh.pdf
	-rm *.log *.aux *.bbl *.blg

