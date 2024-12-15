"use client"
import { useState, useEffect } from "react"
import { get, post } from "@/requests"
import Top from "@/components/top"
import { useRouter } from "next/navigation"

export default function Profile() {
    const router = useRouter()
    const [me, setMe] = useState(null)

    useEffect(() => {
        (async () => {
            setMe(await get('/auth/me'))
        })()
    }, [])

    useEffect(() => {
        if (me != null && me.status_code == 401) {
            router.push('/login')
        }
    }, [me])

    const logout = async e => {
        e.preventDefault()
        await post('/auth/logout')
        router.push('/')
    }

    return <main>
        <Top><h1>Профиль</h1></Top>
        {me == null || me.status_code == 401
            ? <p className="container relative top-8">Загрузка...</p>
            : <>
                <div className="container">
                    <p className="mt-8">Имя: {me.full_name}</p>
                    <p>E-mail: {me.email}</p>
                    <p>Курс: {me.course}</p>
                    <p className="mt-4"><a onClick={logout} href="/">Выйти</a></p>
                </div>
            </>
        }
    </main>
}