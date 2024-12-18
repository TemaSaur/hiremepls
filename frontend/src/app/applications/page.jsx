'use client'
import Top from "@/components/top";
import Application from "@/components/application";
import { get } from "@/requests";
import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";

export default function Applications() {
    const router = useRouter()
    const [applications, setApplications] = useState([])

    useEffect(() => {
        (async () => {
            const res = await get('/applications/')
            if (res.status_code == 401) {
                router.push('/login')
                return
            }
            setApplications(res)
        })()
    }, [])

    return <main>
        <Top><h1>Отклики</h1></Top>
        <div className="container">
            <div className="py-8">
                {applications.map(application => 
                    <Application application={application} key={application.vacancy.slug} />
                )}
            </div>
        </div>
    </main>
}