import React, { Component } from 'react';
import './UpdateTgIDForm.css';

class UpdateTgIDForm extends Component {
    state = {
        tgid: '',
        tgidError: null
    };

    tgidChangeHandler = event => {
        const tgid = event.target.value;
        this.setState({
            tgid,
            tgidError: !tgid
        });
    };

    submitHandler = event => {
        event.preventDefault();

        const { tgid } = this.state;

        if (tgid) {
            this.setState({
                tgid: '',
                tgidError: false
            });
            this.props.onSubmit();
            return;
        }

        this.setState({
            tgidError: !tgid
        });
    };

    render() {
        const { tgid, tgidError } = this.state;

        return (
            <form className='tgid-form' align = 'left' onSubmit={this.submitHandler}>
                <div class='row'>
                <div className='tgid-form__field' align='left'>
                    <input align='left'
                        value={tgid}
                        onChange={this.tgidChangeHandler}
                        placeholder='Telegram ID'
                    />
                    {tgidError ? (
                        <div className='error'>Введите ID</div>
                    ) : null}
                </div>
                <button className='button' type='submit'>
                    Отправить
                </button>
                </div>
            </form>
        );
    }
}

export default UpdateTgIDForm;
