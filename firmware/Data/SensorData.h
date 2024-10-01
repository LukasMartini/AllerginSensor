#ifndef SENSORDATA_H
#define SENSORDATA_H

#include "Data.h"

class SensorData: public Data {
    public:
        virtual bool is_valid() const override;
};

#endif
