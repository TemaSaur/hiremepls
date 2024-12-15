'use client'
import { useRouter } from "next/navigation"
import { useState } from "react"
import Button from "./button"
import { post } from "@/requests"

export default function AuthForm({type}) {
    const router = useRouter()

    const [formData, setFormData] = useState({
        email: '',
        password: '',
        full_name: '',
        course: 0
    })

    const [error, setError] = useState('')

    const onChange = e => {
        const { name, value } = e.target
        setFormData(prev => ({...prev, [name]: value}))
    }

    const onSubmit = async e => {
        e.preventDefault()
        const endpoint = `/auth/${type}`
        const res = await post(endpoint, formData)

        if (res.status_code == 200) {
            router.push('/profile')
        } else {
            console.log(res)
            setError(res.detail[0].msg || res.detail)
        }
    }

    return <form onSubmit={onSubmit} className="flex flex-col items-center gap-4">
        {error && <p className="text-red-300">{error}</p> }

        <div className="flex flex-col">
            <label htmlFor="email">E-mail</label>
            <input
                type="email"
                name="email"
                id="email"
                placeholder="example@mail.com"
                value={formData.email}
                onChange={onChange}
                required />
        </div>

        {type === 'register' &&
            <div className="flex flex-col">
                <label htmlFor="full_name">ФИО</label>
                <input
                    type="text"
                    name="full_name"
                    id="full_name"
                    placeholder="Иванов Иван Иванович"
                    value={formData.full_name}
                    onChange={onChange}
                    required />
            </div>
        }

        {type === 'register' &&
            <div className="flex flex-col">
                <label htmlFor="course">Курс</label>
                <input
                    type="number"
                    name="course"
                    id="course"
                    placeholder="1-5"
                    value={formData.course}
                    onChange={onChange}
                    required />
            </div>
        }

        <div className="flex flex-col mb-6">
            <label htmlFor="password">Пароль</label>
            <input
                type="password"
                name="password"
                id="password"
                placeholder="********"
                value={formData.password}
                onChange={onChange}
                required />
        </div>

        <Button>{type === 'register' ? 'Зарегистрироваться' : 'Войти'}</Button>
    </form>
}