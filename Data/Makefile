CXX = g++
CXXFLAGS = -Wall -g -c

Data.o: Data.h
	${CXX} ${CXXFLAGS} Data.cc

ExternalSourceData.o: Data.h ExternalSourceData.h
	${CXX} ${CXXFLAGS} ExternalSourceData.cc

FormattedData.o: Data.h FormattedData.h
	${CXX} ${CXXFLAGS} FormattedData.h

SensorData.o: Data.h SensorData.h
	${CXX} ${CXXFLAGS} SensorData.cc

.PHONY: clean
clean:
	rm -rf *.o *.d *.gch
