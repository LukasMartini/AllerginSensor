#ifndef FORMATTEDDATA_H
#define FORMATTEDDATA_H

#include "Data.h"

class FormattedData: public Data {
    public:
        virtual bool is_valid() const override;
};

#endif
