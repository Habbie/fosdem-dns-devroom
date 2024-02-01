# Latex Makefile using latexmk
# Modified by Dogukan Cagatay <dcagatay@gmail.com>
# Originally from : http://tex.stackexchange.com/a/40759
#
# Change only the variable below to the name of the main tex file.
PROJNAME=FOSDEM-intermission-slides

# The command to use
LATEXMK=latexmk -lualatex -shell-escape -halt-on-error

# You want latexmk to *always* run, because make does not have all the info.
# Also, include non-file targets in .PHONY so they are run regardless of any
# file of the given name existing.
.PHONY: $(PROJNAME).pdf all clean view

# The first rule in a Makefile is the one executed by default ("make"). It
# should always be the "all" rule, so that "make" and "make all" are identical.
all: $(PROJNAME).pdf

# CUSTOM BUILD RULES

#data.csv:
#	PENTA_USERNAME=X PENTA_PASSWORD=X PENTA_DEVROOM_ID=1264 ~/go/bin/penta-export > data.csv

%.tex: %.j2 data.json make-tex.py
	./make-tex.py $< > $@

# MAIN LATEXMK RULE

# -lualatex tells latexmk to generate PDF directly with lualatex (used for the font awesome glyphs)
# -shell-escape tells lualatex that it is ok to call shell commands (needed for pygments)
# -use-make tells latexmk to call make for generating missing files.

# -interactive=nonstopmode keeps the pdflatex backend from stopping at a
# missing file reference and interactively asking you for an alternative.

$(PROJNAME).pdf: $(PROJNAME).tex
	$(LATEXMK) -use-make $<

cleanall: clean

clean:
	latexmk -c
	rm -f $(PROJNAME).tex

view: $(PROJNAME).tex
	$(LATEXMK) -pvc $<
