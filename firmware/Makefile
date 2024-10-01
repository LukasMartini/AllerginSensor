# Main makefile. Compiles all sub-makefiles.
CXX=g++
CXXFLAGS=-std=c++14 -Wall -g -MMD
EXEC=allerginsensor

DATACCFILES = ${wildcard ./Data/*.cc}
DATAMANAGEMENTCCFILES = ${wildcard ./DataManagement/*.cc}
INPUTCCFILES = ${wildcard ./Input/*.cc}
OUTPUTCCFILES = ${wildcard ./Output/*.cc}
EXCEPTIONFILES = ${wildcard ./Exceptions/*.cc}
MAINCCFILES = ${wildcard *.cc}

DATAOBJECTS = ${DATACCFILES:.cc=.o}
DATAMANAGEMENTOBJECTS = ${DATAMANAGEMENTCCFILES:.cc=.o}
INPUTOBJECTS = ${INPUTCCFILES:.cc=.o}
OUTPUTOBJECTS = ${OUTPUTCCFILES:.cc=.o}
EXCEPTIONOBJECTS = ${EXCEPTIONFILES:.cc=.o}
MAINOBJECTS = ${MAINCCFILES:.cc=.o}

DEPENDENCIES = ${DATAOBJECTS:.o=.d} ${DATAMANAGEMENTOBJECTS:.o=.d} ${INPUTOBJECTS:.o=.d} ${OUTPUTOBJECTS:.o=.d} ${EXCEPTIONFILES:.cc=.o} ${MAINOBJECTS:.o=.d}

${EXEC}: ${MAINOBJECTS} ${DATAOBJECTS} ${DATAMANAGEMENTOBJECTS} ${INPUTOBJECTS} ${OUTPUTOBJECTS}
	${CXX} ${CXXFLAGS} ${MAINOBJECTS} ${DATAOBJECTS} ${DATAMANAGEMENTOBJECTS} ${INPUTOBJECTS} ${OUTPUTOBJECTS} ${EXCEPTIONFILES:.cc=.o} -o ${EXEC}

-include ${DEPENDENCIES}

.PHONY: clean
clean:
	rm -rf allerginsensor *.o *.d ./Data/*.o ./Data/*.d ./DataManagement/*.o ./DataManagement/*.d ./Input/*.o ./Input/*.d ./Output/*.o ./Output/*.d ./Exceptions/*.cc ./Exceptions/*.d

.PHONY: test
test:
	echo ${OBJECTS}
