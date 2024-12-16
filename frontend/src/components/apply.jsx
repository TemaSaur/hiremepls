import { post, sendFile } from "@/requests"
import { useState } from "react"
import { useRouter } from "next/navigation"
import Button from "./button"
import Markdown from "markdown-to-jsx"

const recommendations = `Обычно в резюме стоит включить следующую информацию:

1. Контактные данные: Укажите ваше полное имя, номер телефона, адрес электронной почты и другие ссылки.
1. Цель резюме: Краткое заявление о ваших карьерных целях и о том, какую позицию вы ищете.
1. Образование: Укажите курс с указанием специальности, Если у вас есть дополнительные курсы или сертификаты, связанные с вакансией, также включите их.
1. Навыки: Укажите ключевые навыки, которые соответствуют требованиям вакансии.
1. Дополнительная информация: Включите раздел о языках, которыми вы владеете, а также о любых других значимых достижениях, таких как публикации, участие в конференциях или волонтерская деятельность.
1. Рекомендации: При желании можно указать контакты людей, которые могут дать вам рекомендацию, или просто написать, что рекомендации предоставляются по запросу.

Помните, что резюме должно быть четким, лаконичным и структурированным. Используйте активные глаголы и избегайте излишней информации, чтобы сделать его более привлекательным для работодателя.
`

export default function Apply({vacancy}) {
    const router = useRouter()
    const [file, setFile] = useState(null)
    const [message, setMessage] = useState('')
    const [error, setError] = useState('')
    const [success, setSuccess] = useState(false)

    const onFileChange = e => {
        setFile(e.target.files[0])
    }

    const onMessageChange = e => {
        setMessage(e.target.value)
    }

    // при общей отправке сначала отправить файл потом из полученных данных отправлять остаток
    const onSubmit = async e => {
        e.preventDefault()
        console.log(file)

        const fileSlug = await sendFile('/resumes/', file)
        if (typeof fileSlug !== 'string') {
            setError(fileSlug.detail[0].msg || fileSlug.detail)
            return
        }

        console.log(fileSlug)

        const res = await post(`/vacancies/${vacancy.slug}/applications/`, {
            resume_slug: fileSlug,
            message: message
        })

        console.log(res)

        if (res.status_code == 200) {
            setSuccess(true)
            router.push('/applications')
            return
        }

        setError(res.detail[0].msg || res.detail)
    }

    return <div className="pt-8">
        {error && <p className="text-red-800">{error}</p> }
        {success && <p className="text-[#26a269]">'Резюме и сопроводительное письмо отправлены успешно'</p>}

        <form onSubmit={onSubmit} className="send-file flex flex-col gap-3 mb-4">
            <div className="file-input flex flex-col gap-1">
                <label htmlFor="file">Резюме</label>
                <input onChange={onFileChange} type="file" name="file" id="file" />
            </div>
            <div className="message-input flex flex-col gap-1 mb-4">
                <label htmlFor="message">Сообщение</label>
                <textarea onChange={onMessageChange} name="message" id="message" value={message} rows={4}></textarea>
            </div>
            <Button>Отправить</Button>
        </form>

        <div className="recommendations"><Markdown>{recommendations}</Markdown></div>
    </div>
}