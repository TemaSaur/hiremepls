const BASE = 'http://localhost:8000'

export const get = async (url, data = null) => {
    const opts = {}
    if (data != null) {
        opts['data'] = JSON.stringify(data)
    }

    const res = await fetch(BASE + url, opts)
    return await res.json()
}