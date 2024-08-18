PROGRAMS =

ifneq ($(MAKECMDGOALS),)
    ifneq ($(MAKECMDGOALS), clean)
        PROGRAMS = $(MAKECMDGOALS)
    endif
endif

# The default rule if none is supplied via the command line
all: $(PROGRAMS)

# Make the assemble .s files
$(PROGRAMS): % : %.o
	ld -o $@ $<
clean:
	rm -f *.o $(PROGRAMS)
