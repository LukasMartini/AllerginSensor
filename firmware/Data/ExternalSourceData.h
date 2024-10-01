#ifndef EXTERNALSOURCEDATA_H
#define EXTERNALSOURCEDATA_H

#include "Data.h"

class ExternalSourceData: public Data {
    public:
        virtual bool is_valid() const override;
};

#endif
