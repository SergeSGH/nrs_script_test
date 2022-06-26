import React from 'react';

import api from '../../api'
import Update from '../../components/Update/Update';
import UpdateTgIDForm from '../../components/UpdateTgIDForm/UpdateTgIDForm';

class HomePage extends React.Component {
    state = {
        closed: true,
    };

    openForm() {
        this.setState({
            closed: false,
        });
    }

    closeForm() {
        this.setState({
            closed: true,
        });
    }

    updateDB() {
        api.updateDB()
      }

    updateDL() {
        api.updateDL()
      }

    changeTelegramID() {
        api.changeTelegramID()
      }

    render() {
        return (
            <div>
                <Update title='Обновить базу данных и дедлайны'>
                    <p>
                        <button
                            className='button'
                            onClick={() => this.updateDB()}
                            >
                                Обновить БД
                            </button>
                            <div>Текущих записей:</div>
                    </p>
                    <p>
                        <button
                            className='button'
                            onClick={() => this.updateDL()}
                            >
                                Обновить дедлайны
                            </button>
                    </p>
                </Update>

                <Update title='Установить Telegram ID'>

                        {this.state.closed ? (
                            <div>
                                <div>
                                    <button
                                        className='button'
                                        onClick={() => this.openForm()}
                                    >
                                        Открыть форму
                                    </button>
                                </div>
                                <div>
                                    Текущий ID:
                                </div>
                            </div>
                        ) : (
                            <div>
                                <hr />
                                <UpdateTgIDForm
                                    onSubmit={() => {
                                        this.closeForm()
                                    }
                                }
                                />
                                </div>
                        )}

                </Update>
            </div>
        );
    }
}

export default HomePage;
