#ifndef OUTPUT_H
#define OUTPUT_H

#include <memory>

#include "../Data/FormattedData.h"

class Output {
    public:
        void receive_data(std::shared_ptr<FormattedData*> data);
};

#endif
