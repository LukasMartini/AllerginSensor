#include "SensorInterpreter.h"

SensorInterpreter::SensorInterpreter(std::shared_ptr<SensorInput*> i, std::shared_ptr<Output*> o): 
    DataManagement{std::make_shared<Input*>(*(i.get())), o} {} 
