'use client'
import { useParams } from "next/navigation"
import { useState, useEffect } from "react"
import { get } from "@/requests"
import Top from "@/components/top"
import VacancyInner from "@/components/vacancy_inner"
import Button from "@/components/button"
import Apply from "@/components/apply"
import Markdown from "markdown-to-jsx"

export default function() {
    const params = useParams()
    const hash = window.location.hash

    const [vacancy, setVacancy] = useState(null)
    const [info, setInfo] = useState(hash === '')

    useEffect(() => {
        (async () => {
           setVacancy(await get(`/vacancies/${params.slug}`))
        })()
    }, [])

    useEffect(() => {
        window.location.hash = info ? '' : 'apply'
    }, [info])

    return <main>
        <Top>
            {vacancy == null
                ? 'Загрузка...'
                : <VacancyInner vacancy={vacancy} />}
            
            <div className="buttons mt-4 gap-8 flex">
                <Button active={!info} onClick={() => setInfo(true)}>Описание</Button>
                <Button active={info} onClick={() => setInfo(false)}>Отклик</Button>
            </div>
        </Top>

        <div className="container">
            {vacancy && info &&
                <div className="description py-6">
                    <Markdown>{vacancy.description}</Markdown>
                </div>
            }
            {vacancy && !info &&
                <Apply vacancy={vacancy} />
            }
        </div>
    </main>
}