const BASE = 'http://localhost:8000'

const send = async (url, method, data = null) => {
    const opts = {
        method: method,
        credentials: 'include'
    }

    if (data != null) {
        opts['']
        opts['body'] = JSON.stringify(data)
        opts['headers'] = {
            'Content-Type': 'application/json'
        }
    }

    const res = await fetch(BASE + url, opts)
    const json = await res.json()

    if (json == null) return

    json.status_code = res.status
    return json
}

export const get = async (url, data = null) => {
    return await send(url, 'get', data)
}

export const post = async (url, data = null) => {
    return await send(url, 'post', data)
}

export const sendFile = async (url, file) => {
    const formData = new FormData()
    formData.append('file', file)

    const res = await fetch(BASE + url, {
        method: 'post',
        credentials: 'include',
        body: formData,
    })
    return await res.json()
}