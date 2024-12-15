import Top from "@/components/top"
import AuthForm from "@/components/auth_form"

export default function Login() {
    return <main>
        <Top><h1>Вход</h1></Top>

        <div className="flex flex-col items-center py-8">
            <AuthForm type={'login'} />
            <a className="mt-4" href="/register">Еще нет аккаунта? Создать</a>
        </div>
    </main>
}