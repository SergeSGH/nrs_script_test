class Api {
  constructor (url, headers) {
    this._url = url
    this._headers = headers
  }

  checkResponse (res) {
    return new Promise((resolve, reject) => {
      if (res.status === 204) {
        return resolve(res)
      }
      const func = res.status < 400 ? resolve : reject
      res.json().then(data => func(data))
    })
  }

  changeTelegramID ({
    telegramID = 0
  }) {
    return fetch(
      '/api/changetelegramid/',
      {
        method: 'POST',
        headers: {
          ...this._headers
        },
        body: JSON.stringify({
          telegramID
        })
      }
    ).then(this.checkResponse)
  }

  updateDB () {
    return fetch(
      '/api/update_data/',
      {
        method: 'GET',
        headers: {
          ...this._headers,
        }
      }
    ).then(this.checkResponse)
  }

  updateDL () {
    console.log('ssssssssssssssssssssssssssssss')
    
    return fetch(
      '/api/records/update_deadlines/',
      {
        method: 'GET',
        headers: {
          ...this._headers,
        }
      }
    ).then(this.checkResponse)
  }
}
export default new Api(process.env.API_URL || 'http://localhost:8000', { 'content-type': 'application/json' })
