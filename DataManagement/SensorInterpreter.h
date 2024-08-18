#ifndef SENSORINTERPRETER_H
#define SENSORINTERPRETER_H

#include "DataManagement.h"
#include "../Input/SensorInput.h"

class Output;

class SensorInterpreter: public DataManagement {
    public:
        SensorInterpreter(std::shared_ptr<SensorInput*> i, std::shared_ptr<Output*> o);
};

#endif
