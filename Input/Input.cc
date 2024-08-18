#include "Input.h"

/*
    Preconditions: Data must be in a valid state.
    Postconditions: Data was passed correctly.
    Description: Provides the caller with the current input data stored in the Input object.
*/
std::shared_ptr<Data*> Input::get_state() const {
    return determine_state();
}

/*
    Preconditions: None.
    Postconditions: None.
    Description: Notifies the associated data management module that there is new data to ingest
*/
void Input::pass_data() const {
    (*associated_data_management_module)->receive_data();
}

/*
    Preconditions: New data must be in a valid state.
    Postconditions: None.
    Description: A public interface to update the raw_input field with. Intended for use by subclasses.
*/
void Input::update_data(std::shared_ptr<Data*> new_data) {
    if (!(*new_data)->is_valid()) throw InvalidInputException{};
    raw_input = new_data;
}
