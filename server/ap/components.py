import asyncio
from asgiref.sync import sync_to_async
from reactpy import component, html, use_state, use_effect, event, use_ref
import requests
import datetime
from datetime import date
import threading

DISPATCHER_COOKIE_VALUE = "dispatcher_id"


# Асинхронные функции для получения данных
@sync_to_async
def fetch_teachers():
    r = requests.get("http://localhost:8000/api/teachers/")
    r.raise_for_status()
    return r.json()


@sync_to_async
def fetch_groups():
    r = requests.get("http://localhost:8000/api/groups/")
    r.raise_for_status()
    return r.json()


@sync_to_async
def fetch_subjects():
    r = requests.get("http://localhost:8000/api/subjects/")
    r.raise_for_status()
    return r.json()


@sync_to_async
def fetch_schedule_data(group_id):
    try:
        r = requests.get(f"http://localhost:8000/api/getScheduleGroup?group={group_id}")
        r.raise_for_status()
        return r.json()
    except Exception:
        return []


@sync_to_async
def post_teacher(name):
    cookies = {"dispatcher_id": DISPATCHER_COOKIE_VALUE}
    return requests.post("http://localhost:8000/api/teachers/add/", json={"name": name}, cookies=cookies)


@sync_to_async
def post_group(name):
    cookies = {"dispatcher_id": DISPATCHER_COOKIE_VALUE}
    return requests.post("http://localhost:8000/api/groups/add/", json={"name": name}, cookies=cookies)


@sync_to_async
def post_subject(name):
    cookies = {"dispatcher_id": DISPATCHER_COOKIE_VALUE}
    return requests.post("http://localhost:8000/api/subjects/add/", json={"name": name}, cookies=cookies)


@sync_to_async
def update_teacher(id_, name):
    cookies = {"dispatcher_id": DISPATCHER_COOKIE_VALUE}
    return requests.put(f"http://localhost:8000/api/teachers/{id_}/", json={"name": name}, cookies=cookies)


@sync_to_async
def update_group(id_, name):
    cookies = {"dispatcher_id": DISPATCHER_COOKIE_VALUE}
    return requests.put(f"http://localhost:8000/api/groups/{id_}/", json={"name": name}, cookies=cookies)


@sync_to_async
def update_subject(id_, name):
    cookies = {"dispatcher_id": DISPATCHER_COOKIE_VALUE}
    return requests.put(f"http://localhost:8000/api/subjects/{id_}/", json={"name": name}, cookies=cookies)


@sync_to_async
def delete_teacher(id_):
    cookies = {"dispatcher_id": DISPATCHER_COOKIE_VALUE}
    return requests.delete(f"http://localhost:8000/api/teachers/{id_}/delete/", cookies=cookies)


@sync_to_async
def delete_group(id_):
    cookies = {"dispatcher_id": DISPATCHER_COOKIE_VALUE}
    return requests.delete(f"http://localhost:8000/api/groups/{id_}/delete/", cookies=cookies)


@sync_to_async
def delete_subject(id_):
    cookies = {"dispatcher_id": DISPATCHER_COOKIE_VALUE}
    return requests.delete(f"http://localhost:8000/api/subjects/{id_}/delete/", cookies=cookies)


@sync_to_async
def fetch_schedule():
    r = requests.get("http://localhost:8000/api/schedule/")
    r.raise_for_status()
    return r.json()


@sync_to_async
def post_schedule(data):
    cookies = {"dispatcher_id": DISPATCHER_COOKIE_VALUE}
    r = requests.post("http://localhost:8000/api/schedule/add/", json=data, cookies=cookies)
    r.raise_for_status()
    return r


@sync_to_async
def update_schedule(id_, data):
    cookies = {"dispatcher_id": DISPATCHER_COOKIE_VALUE}
    r = requests.put(f"http://localhost:8000/api/schedule/{id_}/", json=data, cookies=cookies)
    r.raise_for_status()
    return r


@sync_to_async
def delete_schedule(id_):
    cookies = {"dispatcher_id": DISPATCHER_COOKIE_VALUE}
    r = requests.delete(f"http://localhost:8000/api/schedule/{id_}/delete/", cookies=cookies)
    r.raise_for_status()
    return r


@sync_to_async
def delete_all_schedules_api():
    cookies = {"dispatcher_id": DISPATCHER_COOKIE_VALUE}
    r = requests.delete(f"http://localhost:8000/api/schedule/delete_all/", cookies=cookies)
    r.raise_for_status()
    return r


# styles


main_style = {
    "fontFamily": "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
    "background": "#f0f4f8",
    "minHeight": "100vh",
    "padding": "1rem 3rem 3rem 3rem",  # more horizontal padding
    "margin": "0",
    "display": "flex",
    "flexDirection": "column",
    "alignItems": "center",
    "color": "#2c3e50",
}

button = {
    "all": "unset",
    "display": "block",
    "width": "100%",
    "cursor": "pointer",
}

header_style = {
    "background": "#0055A5",
    "color": "#fff",
    "padding": "2rem 3rem 1.2rem 3rem",  # increased horizontal padding
    "textAlign": "center",
    "boxShadow": "0 6px 20px rgba(0, 85, 165, 0.3)",
    "borderRadius": "12px",
    "width": "100%",  # full width
    # Remove maxWidth or increase it if you want a max limit
    "marginBottom": "2rem",
    "userSelect": "none",
}

footer_style = {
    "background": "#0055A5",
    "color": "white",
    "padding": "1rem 3rem",  # increased horizontal padding
    "textAlign": "center",
    "marginTop": "auto",
    "borderRadius": "0 0 12px 12px",
    "width": "100%",  # full width
    # Remove maxWidth or increase it
    "boxShadow": "0 -4px 12px rgba(0,85,165,0.2)",
}

filter_container = {
    "display": "flex",
    "gap": "1rem",
    "justifyContent": "center",
    "marginBottom": "2rem",
    "flexWrap": "wrap",
    "width": "100%",
}

select_style = {
    "padding": "0.6rem 1.2rem",
    "borderRadius": "10px",
    "border": "1.5px solid #0055A5",
    "backgroundColor": "#fff",
    "color": "#0055A5",
    "fontSize": "1.1rem",
    "minWidth": "220px",
    "boxShadow": "0 2px 6px rgba(0,85,165,0.15)",
    "transition": "border-color 0.3s ease",
    "cursor": "pointer",
}

select_style_hover = {
    "borderColor": "#003f7a",
}

# Table styles with rounded corners and subtle shadows
table_style = {
    "width": "90vw",  # 90% of the viewport width
    "maxWidth": "100%",
    "margin": "0 auto",
    "borderCollapse": "separate",
    "borderSpacing": "0 10px",
    "backgroundColor": "transparent",
    "boxShadow": "0 4px 18px rgba(0,0,0,0.1)",
    "borderRadius": "12px",
    "overflow": "hidden",
}

th_base_style = {
    "padding": "1rem 1.2rem",
    "background": "#0055A5",
    "color": "white",
    "textAlign": "center",
    "fontWeight": "700",
    "fontSize": "1.1rem",
    "userSelect": "none",
}

td_base_style = {
    "padding": "1rem 1.2rem",
    "background": "#fff",
    "textAlign": "center",
    "fontSize": "1rem",
    "color": "#34495e",
    "boxShadow": "0 0 6px rgba(0,0,0,0.05)",
    "borderBottom": "none",
}

tr_style = {
    "borderRadius": "12px",
    "boxShadow": "0 2px 6px rgba(0,0,0,0.07)",
}

empty_row_style = {
    "color": "#7f8c8d",
    "fontStyle": "italic",
    "padding": "3rem",
    "textAlign": "center",
}


@component
def ScheduleComponent():
    schedules, set_schedules = use_state([])
    groups, set_groups = use_state([])
    selected_date, set_selected_date = use_state(date.today().isoformat())
    selected_group, set_selected_group = use_state("")
    is_select_hovered, set_select_hovered = use_state(False)

    select_style_base = {
        "padding": "0.6rem 1.2rem",
        "borderRadius": "10px",
        "backgroundColor": "#fff",
        "color": "#0055A5",
        "fontSize": "1.1rem",
        "minWidth": "220px",
        "boxShadow": "0 2px 6px rgba(0,85,165,0.15)",
        "transition": "border-color 0.3s ease",
        "cursor": "pointer",
    }

    # Новый стиль для кнопки перехода
    top_right_button_style = {
        "position": "absolute",
        "top": "2rem",
        "right": "2rem",
        "background": "#2980b9",
        "color": "#fff",
        "padding": "0.6rem 1.3rem",
        "borderRadius": "8px",
        "fontWeight": "700",
        "fontSize": "1.1rem",
        "textDecoration": "none",
        "boxShadow": "0 4px 12px rgba(41, 128, 185, 0.15)",
        "transition": "background 0.2s",
        "zIndex": "100",
    }

    def select_style():
        style = select_style_base.copy()
        style["border"] = "1.5px solid #003f7a" if is_select_hovered else "1.5px solid #0055A5"
        return style

    async def load_data():
        groups_data = await fetch_groups()
        set_groups(groups_data)

        if groups_data:
            first_group = groups_data[0]
            set_selected_group(first_group['name'])

            schedule_data = await fetch_schedule_data(first_group['id'])
            set_schedules(schedule_data)

    def start_load_data():
        asyncio.create_task(load_data())

    use_effect(start_load_data, [])

    async def handle_group_change(e):
        group_name = e['target']['value']
        set_selected_group(group_name)

        group_id = next((g['id'] for g in groups if g['name'] == group_name), None)
        if group_id is not None:
            data = await fetch_schedule_data(group_id)
            set_schedules(data)

    filtered = [
        item for item in schedules
        if item.get("day") == selected_date and item.get("group") == selected_group
    ]

    # Обертка для позиционирования кнопки (relative)
    return html.div(
        {"style": {**main_style, "position": "relative"}},
        # КНОПКА В ПРАВОМ ВЕРХНЕМ УГЛУ
        html.a(
            {
                "href": "/dispatcher/dashboard/",
                "style": top_right_button_style,
            },
            "Войти как диспетчер"
        ),
        html.header(
            {"style": header_style},
            html.h1("Расписание занятий"),
            html.p("Выберите группу и дату")
        ),
        html.div(
            {"style": filter_container},
            html.select({
                "value": selected_group,
                "onChange": handle_group_change,
                "style": select_style(),
                "onMouseEnter": lambda e: set_select_hovered(True),
                "onMouseLeave": lambda e: set_select_hovered(False),
            },
                [html.option({"value": group['name']}, group['name']) for group in groups]
            ),
            html.input({
                "type": "date",
                "value": selected_date,
                "onChange": lambda e: set_selected_date(e["target"]["value"]),
                "style": select_style_base,
            })
        ),
        html.div(
            html.table(
                {"style": table_style},
                html.thead(
                    html.tr(
                        html.th({"style": th_base_style}, "Кабинет"),
                        html.th({"style": th_base_style}, "Предмет"),
                        html.th({"style": th_base_style}, "Преподаватель"),
                        html.th({"style": th_base_style}, "Время"),
                    )
                ),
                html.tbody(
                    [html.tr(
                        {"style": tr_style},
                        html.td({"style": td_base_style}, item["room"]),
                        html.td({"style": td_base_style}, item["subject"]),
                        html.td({"style": td_base_style}, item["teacher"]),
                        html.td({"style": td_base_style}, item["startTime"]),
                    ) for item in filtered] if filtered else [
                        html.tr(
                            html.td(
                                {"colSpan": 4, "style": empty_row_style},
                                "Нет занятий на выбранную дату"
                            )
                        )
                    ]
                )
            )
        ),
        html.footer(
            {"style": footer_style},
            html.p("© Ставропольский Колледж Связи")
        )
    )


@component
def renderSchedulePage():
    return ScheduleComponent()


@component
def DeleteButton(*, onClick):
    hovered, set_hovered = use_state(False)
    style = {
        "backgroundColor": "#e74c3c",
        "color": "#fff",
        "border": "none",
        "padding": "0.4rem 1rem",
        "marginRight": "0.5rem",
        "borderRadius": "12px",  # скруглённые углы
        "cursor": "pointer",
        "fontSize": "0.9rem",
        "fontWeight": "600",
        "boxShadow": "0 4px 8px rgba(231, 76, 60, 0.4)",
        "transition": "background-color 0.3s ease, box-shadow 0.3s ease",
        "userSelect": "none",
        "outline": "none",
    }
    if hovered:
        style.update({
            "backgroundColor": "#c0392b",
            "boxShadow": "0 6px 12px rgba(192, 57, 43, 0.6)",
        })
    return html.button({
        "style": style,
        "onMouseEnter": lambda e: set_hovered(True),
        "onMouseLeave": lambda e: set_hovered(False),
        "onClick": onClick,
        "type": "button",
        "title": "Удалить запись",
    }, "Удалить")


@component
def ScheduleForm(
        *,
        styles,
        groups,
        teachers,
        subjects,
        schedule,
        loading,
        set_message,
        set_error_message,
        set_loading,
        load_all_data,
):
    subject_map = {str(s["id"]): s["name"] for s in subjects}
    teacher_map = {str(t["id"]): t["name"] for t in teachers}
    group_map = {str(g["id"]): g["name"] for g in groups}

    schedule_group_id, set_schedule_group_id = use_state(str(groups[0]["id"]) if groups else "")
    schedule_teacher_id, set_schedule_teacher_id = use_state(str(teachers[0]["id"]) if teachers else "")
    schedule_subject_id, set_schedule_subject_id = use_state(str(subjects[0]["id"]) if subjects else "")
    schedule_day, set_schedule_day = use_state(datetime.date.today().isoformat())
    schedule_week, set_schedule_week = use_state(1)
    schedule_room, set_schedule_room = use_state("")
    schedule_start, set_schedule_start = use_state("")
    schedule_end, set_schedule_end = use_state("")

    selected_view_group, set_selected_view_group = use_state(str(groups[0]["id"]) if groups else "")

    editing_schedule_id, set_editing_schedule_id = use_state(None)
    editing_values, set_editing_values = use_state({})

    upload_status, set_upload_status = use_state("")
    iframe_ref = use_ref(None)
    selected_file, set_selected_file = use_state(None)
    selected_file_content, set_selected_file_content = use_state(None)
    selected_file_name, set_selected_file_name = use_state("")

    use_effect(lambda: set_schedule_group_id(str(groups[0]["id"])) if groups and not schedule_group_id else None,
               [groups])
    use_effect(
        lambda: set_schedule_teacher_id(str(teachers[0]["id"])) if teachers and not schedule_teacher_id else None,
        [teachers])
    use_effect(
        lambda: set_schedule_subject_id(str(subjects[0]["id"])) if subjects and not schedule_subject_id else None,
        [subjects])
    use_effect(lambda: set_selected_view_group(str(groups[0]["id"])) if groups and not selected_view_group else None,
               [groups])

    @event(prevent_default=True)
    async def delete_all_schedules(e):
        set_loading(True)
        set_message("")
        set_error_message("")
        try:
            # Здесь вызывайте ваш API для удаления всех записей расписания
            # Пример с requests или httpx:
            # response = requests.delete("http://localhost:8000/api/schedule/delete_all/")
            # Или ваш асинхронный вызов:
            response = await delete_all_schedules_api()

            if response.status_code in (200, 204):
                set_message("Все записи расписания удалены")
                await load_all_data()
            else:
                set_error_message(f"Ошибка удаления: {response.status_code}")
        except Exception as ex:
            set_error_message(f"Ошибка: {ex}")
        finally:
            set_loading(False)

    async def on_iframe_load(e):
        # Когда iframe загрузился — обновляем данные
        # Можно добавить проверку, чтобы не вызывать лишний раз
        set_upload_status("Файл загружен, обновляем таблицу...")
        # Вызов асинхронной функции загрузки данных
        import asyncio
        asyncio.create_task(load_all_data())
        # Очистим сообщение через пару секунд

        threading.Timer(3, lambda: set_upload_status("")).start()

    @event
    async def on_file_change(e):
        files = e.get("target", {}).get("files")
        if files and len(files) > 0:
            set_selected_file(files[0])
            set_upload_status(f"Выбран файл: {files[0].name}")
        else:
            set_selected_file(None)
            set_upload_status("Файл не выбран")

    @event(prevent_default=True)
    async def on_upload(e):
        if not selected_file_content:
            set_upload_status("Сначала выберите файл")
            return

        set_loading(True)
        set_upload_status("")
        set_message("")
        set_error_message("")

        try:
            # Отправка файла на сервер синхронно в отдельном потоке, чтобы не блокировать event loop
            def send_file():
                files = {'excel_file': (selected_file_name, selected_file_content)}
                response = requests.post("http://localhost:8000/upload_schedule/", files=files)
                return response

            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(None, send_file)

            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "success":
                    count = data.get("added", 0)
                    set_upload_status(f"Успешно добавлено записей: {count}")
                    await load_all_data()
                else:
                    set_error_message(data.get("error", "Ошибка загрузки"))
            else:
                set_error_message(f"Ошибка сервера: {response.status_code}")
        except Exception as ex:
            set_error_message(f"Ошибка: {ex}")
        set_loading(False)

    @event(prevent_default=True)
    async def submit_schedule(e):
        set_loading(True)
        set_message("")
        set_error_message("")
        try:
            data = {
                "groupId": schedule_group_id,
                "teacherId": schedule_teacher_id,
                "subjectId": schedule_subject_id,
                "day": schedule_day,
                "week": schedule_week,
                "room": schedule_room,
                "startTime": schedule_start,
                "endTime": schedule_end,
            }
            resp = await post_schedule(data)
            if resp.status_code == 201:
                set_message("Запись добавлена")
                set_schedule_room("")
                set_schedule_start("")
                set_schedule_end("")
                await load_all_data()
            else:
                set_error_message(f"Ошибка: {resp.text}")
        except Exception as ex:
            set_error_message(f"Ошибка: {ex}")
        set_loading(False)

    @event(prevent_default=True)
    async def save_schedule_edit(e):
        set_loading(True)
        set_message("")
        set_error_message("")
        try:
            resp = await update_schedule(editing_schedule_id, editing_values)
            if resp.status_code in (200, 204):
                set_message("Запись обновлена")
                set_editing_schedule_id(None)
                set_editing_values({})
                await load_all_data()
            else:
                set_error_message(f"Ошибка: {resp.text}")
        except Exception as ex:
            set_error_message(f"Ошибка: {ex}")
        set_loading(False)

    async def on_delete_schedule(id_):
        set_loading(True)
        set_message("")
        set_error_message("")
        try:
            resp = await delete_schedule(id_)
            if resp.status_code in (200, 204):
                set_message("Запись удалена")
                await load_all_data()
            else:
                set_error_message(f"Ошибка: {resp.text}")
        except Exception as ex:
            set_error_message(f"Ошибка: {ex}")
        set_loading(False)

    filtered_schedule = [item for item in schedule if str(item.get("groupId")) == selected_view_group]

    def ScheduleTable():
        rows = []
        for s in filtered_schedule:
            if editing_schedule_id == s["id"]:
                rows.append(html.tr(
                    html.td(html.input({
                        "type": "text",
                        "value": editing_values.get("room", s["room"]),
                        "onChange": lambda e: set_editing_values({**editing_values, "room": e["target"]["value"]}),
                        "style": styles["input_inline"],
                    })),
                    html.td(html.input({
                        "type": "date",
                        "value": editing_values.get("day", s["day"]),
                        "onChange": lambda e: set_editing_values({**editing_values, "day": e["target"]["value"]}),
                        "style": styles["input_inline"],
                    })),
                    html.td(html.input({
                        "type": "number",
                        "value": editing_values.get("week", s["week"]),
                        "onChange": lambda e: set_editing_values({**editing_values, "week": int(e["target"]["value"])}),
                        "style": styles["input_inline"],
                    })),
                    html.td(html.input({
                        "type": "text",
                        "value": editing_values.get("startTime", s["startTime"]),
                        "onChange": lambda e: set_editing_values({**editing_values, "startTime": e["target"]["value"]}),
                        "style": styles["input_inline"],
                    })),
                    html.td(html.input({
                        "type": "text",
                        "value": editing_values.get("endTime", s["endTime"]),
                        "onChange": lambda e: set_editing_values({**editing_values, "endTime": e["target"]["value"]}),
                        "style": styles["input_inline"],
                    })),
                    html.td(html.select({
                        "value": editing_values.get("subjectId", str(s["subjectId"])),
                        "onChange": lambda e: set_editing_values({**editing_values, "subjectId": e["target"]["value"]}),
                        "style": styles["input_inline"],
                    }, [html.option({"value": str(sub["id"])}, sub["name"]) for sub in subjects])),
                    html.td(html.select({
                        "value": editing_values.get("teacherId", str(s["teacherId"])),
                        "onChange": lambda e: set_editing_values({**editing_values, "teacherId": e["target"]["value"]}),
                        "style": styles["input_inline"],
                    }, [html.option({"value": str(teach["id"])}, teach["name"]) for teach in teachers])),
                    html.td(
                        html.button({"style": styles["action_button"], "onClick": save_schedule_edit}, "Сохранить"),
                        html.button(
                            {"style": styles["action_button"], "onClick": lambda e: set_editing_schedule_id(None)},
                            "Отмена"),
                    ),
                ))
            else:
                rows.append(html.tr(
                    html.td(s["room"]),
                    html.td(s["day"]),
                    html.td(s["week"]),
                    html.td(s["startTime"]),
                    html.td(s["endTime"]),
                    html.td(subject_map.get(str(s.get("subjectId")), "—")),
                    html.td(teacher_map.get(str(s.get("teacherId")), "—")),
                    html.td(
                        html.button({"style": styles["action_button"], "onClick": lambda e, id=s["id"]: (
                            set_editing_schedule_id(id), set_editing_values({}))}, "Редактировать"),
                        DeleteButton(onClick=lambda e, id=s["id"]: asyncio.create_task(on_delete_schedule(id))),
                    ),
                ))
        return html.table(
            {"style": styles["table"]},
            html.thead(
                html.tr(
                    html.th("Кабинет"),
                    html.th("Дата"),
                    html.th("Неделя"),
                    html.th("Начало"),
                    html.th("Конец"),
                    html.th("Предмет"),
                    html.th("Преподаватель"),
                    html.th("Действия"),
                )
            ),
            html.tbody(rows)
        )

    return html.div(
        {"style": styles.get("form", {})},
        html.h3("Загрузка расписания из Excel"),
        # Передаём ref отдельным аргументом, не в атрибутах
        html.iframe(
            {
                "name": "hidden_iframe",
                "style": {"display": "none"},
                "onLoad": on_iframe_load,
            },
        ),
        html.form(
            {
                "action": "/upload_schedule/",
                "method": "POST",
                "enctype": "multipart/form-data",
                "target": "hidden_iframe",
                "onSubmit": lambda e: set_upload_status("Файл загружается..."),
            },
            html.input({
                "type": "file",
                "name": "excel_file",
                "accept": ".xlsx,.xls",
                "required": True,
                "style": {"marginBottom": "1rem"},
            }),
            html.button({"type": "submit", "style": styles.get("button", {})}, "Загрузить и распарсить"),
        ),
        html.div({"style": {"marginTop": "1rem", "color": "green"}}, upload_status),

        html.h3("Добавить расписание вручную"),
        html.form(
            {"onSubmit": submit_schedule},
            html.label({"style": styles["label"]}, "Группа"),
            html.select({
                "value": schedule_group_id,
                "onChange": lambda e: set_schedule_group_id(e["target"]["value"]),
                "style": styles["input"],
            }, [html.option({"value": g["id"]}, g["name"]) for g in groups]),

            html.label({"style": styles["label"]}, "Преподаватель"),
            html.select({
                "value": schedule_teacher_id,
                "onChange": lambda e: set_schedule_teacher_id(e["target"]["value"]),
                "style": styles["input"],
            }, [html.option({"value": t["id"]}, t["name"]) for t in teachers]),

            html.label({"style": styles["label"]}, "Предмет"),
            html.select({
                "value": schedule_subject_id,
                "onChange": lambda e: set_schedule_subject_id(e["target"]["value"]),
                "style": styles["input"],
            }, [html.option({"value": s["id"]}, s["name"]) for s in subjects]),

            html.label({"style": styles["label"]}, "Дата"),
            html.input({
                "type": "date",
                "value": schedule_day,
                "onChange": lambda e: set_schedule_day(e["target"]["value"]),
                "style": styles["input"],
            }),

            html.label({"style": styles["label"]}, "Неделя"),
            html.input({
                "type": "number",
                "value": schedule_week,
                "onChange": lambda e: set_schedule_week(int(e["target"]["value"])),
                "style": styles["input"],
            }),

            html.label({"style": styles["label"]}, "Кабинет"),
            html.input({
                "type": "text",
                "value": schedule_room,
                "onChange": lambda e: set_schedule_room(e["target"]["value"]),
                "style": styles["input"],
            }),

            html.label({"style": styles["label"]}, "Начало"),
            html.input({
                "type": "text",
                "value": schedule_start,
                "onChange": lambda e: set_schedule_start(e["target"]["value"]),
                "style": styles["input"],
            }),

            html.label({"style": styles["label"]}, "Конец"),
            html.input({
                "type": "text",
                "value": schedule_end,
                "onChange": lambda e: set_schedule_end(e["target"]["value"]),
                "style": styles["input"],
            }),

            html.button({
                "type": "submit",
                "style": styles["button"],
                "disabled": loading,
            }, "Добавить запись"),
        ),
        html.h3("Выберите группу для просмотра расписания"),
        html.select({
            "value": selected_view_group,
            "onChange": lambda e: set_selected_view_group(e["target"]["value"]),
            "style": styles["input"],
        }, [html.option({"value": g["id"]}, g["name"]) for g in groups]),
        html.h3("Текущее расписание"),
        html.div(
            {"style": {"marginBottom": "1rem"}},
            html.button({
                "onClick": delete_all_schedules,
                "disabled": loading,
                "style": {**styles.get("button", {}), "backgroundColor": "#e74c3c"},  # красная кнопка
            }, "Удалить всё расписание"),
        ),
        ScheduleTable()
    )


# диспетчер

@component
def DispatcherDashboard(logout_url="/dispatcher/logout/"):
    styles = {
        "body": {
            "margin": "0",
            "minHeight": "100vh",
            "fontFamily": "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
            "background": "#f4f7fa",
            "display": "flex",
            "color": "#333",
        },
        "sidebar": {
            "width": "260px",
            "background": "#2c3e50",
            "color": "#ecf0f1",
            "display": "flex",
            "flexDirection": "column",
            "padding": "2rem 1rem",
            "boxShadow": "2px 0 12px rgba(0,0,0,0.1)",
        },
        "sidebar_button": {
            "backgroundColor": "transparent",
            "color": "#ecf0f1",
            "fontWeight": "400",
            "border": "none",
            "width": "100%",
            "fontSize": "1.1rem",
            "padding": "0.75rem 1rem",
            "margin": "0.25rem 0",
            "textAlign": "left",
            "cursor": "pointer",
            "borderRadius": "6px",
            "transition": "background-color 0.2s, color 0.2s",
            "userSelect": "none",
            "outline": "none",
        },

        "sidebar_button_active": {
            "backgroundColor": "#34495e",
            "color": "#fff",
            "fontWeight": "700",
        },
        "content": {
            "flexGrow": "1",
            "padding": "2rem",
            "background": "#fff",
            "borderRadius": "0 12px 12px 0",
            "boxShadow": "0 0 20px rgba(0,0,0,0.05)",
            "overflowY": "auto",
            "maxWidth": "1000px",
            "margin": "auto",
        },
        "form": {
            "maxWidth": "900px",
            "marginBottom": "2rem",
            "background": "#f9fbfd",
            "padding": "1.5rem",
            "borderRadius": "10px",
            "boxShadow": "0 2px 8px rgba(0,0,0,0.05)",
        },
        "label": {
            "display": "block",
            "marginBottom": "0.5rem",
            "fontWeight": "600",
            "color": "#34495e",
        },
        "input": {
            "width": "100%",
            "padding": "0.5rem 0.75rem",
            "fontSize": "1rem",
            "borderRadius": "6px",
            "border": "1.5px solid #ccc",
            "boxSizing": "border-box",
            "marginBottom": "1rem",
            "transition": "border-color 0.3s",
        },
        "button": {
            "backgroundColor": "#2980b9",
            "color": "#fff",
            "border": "none",
            "padding": "0.7rem 1.5rem",
            "fontSize": "1.1rem",
            "borderRadius": "8px",
            "cursor": "pointer",
            "fontWeight": "700",
            "boxShadow": "0 4px 12px rgba(41, 128, 185, 0.4)",
            "transition": "background-color 0.3s ease",
            "userSelect": "none",
        },
        "button_disabled": {
            "backgroundColor": "#95a5a6",
            "cursor": "default",
            "boxShadow": "none",
        },
        "message": {
            "marginTop": "1rem",
            "fontWeight": "600",
            "color": "#27ae60",
        },
        "error_message": {
            "marginTop": "1rem",
            "fontWeight": "600",
            "color": "#e74c3c",
        },
        "table": {
            "width": "100%",
            "borderCollapse": "collapse",
            "marginTop": "1rem",
            "boxShadow": "0 2px 10px rgba(0,0,0,0.05)",
            "maxWidth": "900px",
        },
        "th": {
            "backgroundColor": "#2980b9",
            "color": "#fff",
            "padding": "0.75rem",
            "textAlign": "left",
            "fontWeight": "700",
            "borderBottom": "2px solid #1c5980",
        },
        "td": {
            "padding": "0.6rem 0.75rem",
            "borderBottom": "1px solid #ddd",
            "verticalAlign": "middle",
        },
        "action_button": {
            "backgroundColor": "#3498db",
            "color": "#fff",
            "border": "none",
            "padding": "0.4rem 0.8rem",
            "marginRight": "0.5rem",
            "borderRadius": "6px",
            "cursor": "pointer",
            "fontSize": "0.9rem",
            "transition": "background-color 0.3s",
            "userSelect": "none",
        },
        "action_button_delete": {
            "backgroundColor": "#e74c3c",
        },
        "input_inline": {
            "width": "90%",
            "padding": "0.3rem 0.5rem",
            "fontSize": "1rem",
            "borderRadius": "6px",
            "border": "1.5px solid #ccc",
            "boxSizing": "border-box",
        },
    }

    active_form, set_active_form = use_state("teacher")
    message, set_message = use_state("")
    error_message, set_error_message = use_state("")
    loading, set_loading = use_state(False)

    teachers, set_teachers = use_state([])
    groups, set_groups = use_state([])
    subjects, set_subjects = use_state([])
    schedule, set_schedule = use_state([])

    teacher_name, set_teacher_name = use_state("")
    group_name, set_group_name = use_state("")
    subject_name, set_subject_name = use_state("")

    editing_teacher_id, set_editing_teacher_id = use_state(None)
    editing_teacher_name, set_editing_teacher_name = use_state("")

    editing_group_id, set_editing_group_id = use_state(None)
    editing_group_name, set_editing_group_name = use_state("")

    editing_subject_id, set_editing_subject_id = use_state(None)
    editing_subject_name, set_editing_subject_name = use_state("")

    selected_group_id, set_selected_group_id = use_state(None)

    async def load_data():
        try:
            t = await fetch_teachers()
            g = await fetch_groups()
            s = await fetch_subjects()
            sched = await fetch_schedule()
            set_teachers(t)
            set_groups(g)
            set_subjects(s)
            set_schedule(sched)
        except Exception as e:
            set_error_message(f"Ошибка загрузки данных: {e}")

    def load_data_effect():
        asyncio.create_task(load_data())
        return None

    use_effect(load_data_effect, [])

    async def load_schedule(group_id):
        try:
            sched = await fetch_schedule_data(group_id)
            set_schedule(sched)
            set_error_message("")
        except Exception as e:
            set_error_message(f"Ошибка загрузки расписания: {e}")

    def on_group_change(e):
        group_id = e["target"]["value"]
        set_selected_group_id(group_id)
        asyncio.create_task(load_schedule(group_id))

    def sidebar_button_style(name):
        base = dict(styles["sidebar_button"])
        if active_form == name:
            base.update(styles["sidebar_button_active"])
        else:
            base["color"] = "#fff"
            base["backgroundColor"] = "#223042"
        return base

    def button_style(is_disabled=False):
        base = styles["button"].copy()
        if is_disabled:
            base.update(styles["button_disabled"])
        return base

    @event(prevent_default=True)
    async def submit_teacher(e):
        set_loading(True)
        set_message("")
        set_error_message("")
        try:
            response = await post_teacher(teacher_name)
            if response.status_code == 201:
                set_message("Преподаватель добавлен")
                set_teacher_name("")
                await load_data()
            else:
                set_error_message(f"Ошибка: {response.text}")
        except Exception as ex:
            set_error_message(f"Ошибка: {ex}")
        set_loading(False)

    @event(prevent_default=True)
    async def submit_group(e):
        set_loading(True)
        set_message("")
        set_error_message("")
        try:
            response = await post_group(group_name)
            if response.status_code == 201:
                set_message("Группа добавлена")
                set_group_name("")
                await load_data()
            else:
                set_error_message(f"Ошибка: {response.text}")
        except Exception as ex:
            set_error_message(f"Ошибка: {ex}")
        set_loading(False)

    @event(prevent_default=True)
    async def submit_subject(e):
        set_loading(True)
        set_message("")
        set_error_message("")
        try:
            response = await post_subject(subject_name)
            if response.status_code == 201:
                set_message("Предмет добавлен")
                set_subject_name("")
                await load_data()
            else:
                set_error_message(f"Ошибка: {response.text}")
        except Exception as ex:
            set_error_message(f"Ошибка: {ex}")
        set_loading(False)

    @event(prevent_default=True)
    async def save_teacher_edit(e):
        set_loading(True)
        set_message("")
        set_error_message("")
        try:
            response = await update_teacher(editing_teacher_id, editing_teacher_name)
            if response.status_code in (200, 204):
                set_message("Преподаватель обновлён")
                set_editing_teacher_id(None)
                set_editing_teacher_name("")
                await load_data()
            else:
                set_error_message(f"Ошибка обновления: {response.text}")
        except Exception as ex:
            set_error_message(f"Ошибка: {ex}")
        set_loading(False)

    @event(prevent_default=True)
    async def save_group_edit(e):
        set_loading(True)
        set_message("")
        set_error_message("")
        try:
            response = await update_group(editing_group_id, editing_group_name)
            if response.status_code in (200, 204):
                set_message("Группа обновлена")
                set_editing_group_id(None)
                set_editing_group_name("")
                await load_data()
            else:
                set_error_message(f"Ошибка обновления: {response.text}")
        except Exception as ex:
            set_error_message(f"Ошибка: {ex}")
        set_loading(False)

    @event(prevent_default=True)
    async def save_subject_edit(e):
        set_loading(True)
        set_message("")
        set_error_message("")
        try:
            response = await update_subject(editing_subject_id, editing_subject_name)
            if response.status_code in (200, 204):
                set_message("Предмет обновлён")
                set_editing_subject_id(None)
                set_editing_subject_name("")
                await load_data()
            else:
                set_error_message(f"Ошибка обновления: {response.text}")
        except Exception as ex:
            set_error_message(f"Ошибка: {ex}")
        set_loading(False)

    async def handle_delete(delete_func, id_):
        set_loading(True)
        set_message("")
        set_error_message("")
        try:
            response = await delete_func(id_)
            if response.status_code in (200, 204):
                set_message("Удаление прошло успешно")
                await load_data()
            else:
                set_error_message(f"Ошибка удаления: {response.text}")
        except Exception as ex:
            set_error_message(f"Ошибка: {ex}")
        set_loading(False)

    def render_action_button(text, on_click, is_delete=False):
        base_style = styles["action_button"].copy()
        if is_delete:
            base_style.update(styles["action_button_delete"])
        return html.button({
            "style": base_style,
            "onClick": on_click,
            "disabled": loading,
        }, text)

    def TeachersTable():
        rows = []
        for t in teachers:
            if editing_teacher_id == t["id"]:
                rows.append(html.tr(
                    html.td({"style": styles["td"]}, t["id"]),
                    html.td({"style": styles["td"]},
                            html.input({
                                "type": "text",
                                "value": editing_teacher_name,
                                "onChange": lambda e: set_editing_teacher_name(e["target"]["value"]),
                                "style": styles["input_inline"],
                            })
                            ),
                    html.td({"style": styles["td"]},
                            render_action_button("Сохранить", save_teacher_edit),
                            render_action_button("Отмена",
                                                 lambda e: (set_editing_teacher_id(None), set_editing_teacher_name("")))
                            ),
                ))
            else:
                rows.append(html.tr(
                    html.td({"style": styles["td"]}, t["id"]),
                    html.td({"style": styles["td"]}, t["name"]),
                    html.td({"style": styles["td"]},
                            render_action_button("Редактировать", lambda e, id=t["id"], name=t["name"]: (
                                set_editing_teacher_id(id), set_editing_teacher_name(name))),
                            html.button({
                                "style": {**styles["action_button"], **styles["action_button_delete"]},
                                "onClick": lambda e, id=t["id"]: asyncio.create_task(handle_delete(delete_teacher, id)),
                                "disabled": loading,
                            }, "Удалить")
                            ),
                ))
        return html.table(
            {"style": styles["table"]},
            html.thead(
                html.tr(
                    html.th({"style": styles["th"]}, "ID"),
                    html.th({"style": styles["th"]}, "Имя"),
                    html.th({"style": styles["th"]}, "Действия"),
                )
            ),
            html.tbody(rows)
        )

    def GroupsTable():
        rows = []
        for g in groups:
            if editing_group_id == g["id"]:
                rows.append(html.tr(
                    html.td({"style": styles["td"]}, g["id"]),
                    html.td({"style": styles["td"]},
                            html.input({
                                "type": "text",
                                "value": editing_group_name,
                                "onChange": lambda e: set_editing_group_name(e["target"]["value"]),
                                "style": styles["input_inline"],
                            })
                            ),
                    html.td({"style": styles["td"]},
                            render_action_button("Сохранить", save_group_edit),
                            render_action_button("Отмена",
                                                 lambda e: (set_editing_group_id(None), set_editing_group_name("")))
                            ),
                ))
            else:
                rows.append(html.tr(
                    html.td({"style": styles["td"]}, g["id"]),
                    html.td({"style": styles["td"]}, g["name"]),
                    html.td({"style": styles["td"]},
                            render_action_button("Редактировать", lambda e, id=g["id"], name=g["name"]: (
                                set_editing_group_id(id), set_editing_group_name(name))),
                            html.button({
                                "style": {**styles["action_button"], **styles["action_button_delete"]},
                                "onClick": lambda e, id=g["id"]: asyncio.create_task(handle_delete(delete_group, id)),
                                "disabled": loading,
                            }, "Удалить")
                            ),
                ))
        return html.table(
            {"style": styles["table"]},
            html.thead(
                html.tr(
                    html.th({"style": styles["th"]}, "ID"),
                    html.th({"style": styles["th"]}, "Название"),
                    html.th({"style": styles["th"]}, "Действия"),
                )
            ),
            html.tbody(rows)
        )

    def SubjectsTable():
        rows = []
        for s in subjects:
            if editing_subject_id == s["id"]:
                rows.append(html.tr(
                    html.td({"style": styles["td"]}, s["id"]),
                    html.td({"style": styles["td"]},
                            html.input({
                                "type": "text",
                                "value": editing_subject_name,
                                "onChange": lambda e: set_editing_subject_name(e["target"]["value"]),
                                "style": styles["input_inline"],
                            })
                            ),
                    html.td({"style": styles["td"]},
                            render_action_button("Сохранить", save_subject_edit),
                            render_action_button("Отмена",
                                                 lambda e: (set_editing_subject_id(None), set_editing_subject_name("")))
                            ),
                ))
            else:
                rows.append(html.tr(
                    html.td({"style": styles["td"]}, s["id"]),
                    html.td({"style": styles["td"]}, s["name"]),
                    html.td({"style": styles["td"]},
                            render_action_button("Редактировать", lambda e, id=s["id"], name=s["name"]: (
                                set_editing_subject_id(id), set_editing_subject_name(name))),
                            html.button({
                                "style": {**styles["action_button"], **styles["action_button_delete"]},
                                "onClick": lambda e, id=s["id"]: asyncio.create_task(handle_delete(delete_subject, id)),
                                "disabled": loading,
                            }, "Удалить")
                            ),
                ))
        return html.table(
            {"style": styles["table"]},
            html.thead(
                html.tr(
                    html.th({"style": styles["th"]}, "ID"),
                    html.th({"style": styles["th"]}, "Название"),
                    html.th({"style": styles["th"]}, "Действия"),
                )
            ),
            html.tbody(rows)
        )

    def TeacherForm():
        return html.div(
            {"style": styles["form"]},
            html.form(
                {"onSubmit": submit_teacher},
                html.label({"style": styles["label"]}, "Имя преподавателя"),
                html.input({
                    "type": "text",
                    "value": teacher_name,
                    "onChange": lambda e: set_teacher_name(e["target"]["value"]),
                    "required": True,
                    "style": styles["input"],
                }),
                html.button({
                    "type": "submit",
                    "disabled": loading,
                    "style": button_style(loading),
                }, "Добавить"),
                message and html.div({"style": styles["message"]}, message),
                error_message and html.div({"style": styles["error_message"]}, error_message),
            ),
            TeachersTable()
        )

    def GroupForm():
        return html.div(
            {"style": styles["form"]},
            html.form(
                {"onSubmit": submit_group},
                html.label({"style": styles["label"]}, "Название группы"),
                html.input({
                    "type": "text",
                    "value": group_name,
                    "onChange": lambda e: set_group_name(e["target"]["value"]),
                    "required": True,
                    "style": styles["input"],
                }),
                html.button({
                    "type": "submit",
                    "disabled": loading,
                    "style": button_style(loading),
                }, "Добавить"),
                message and html.div({"style": styles["message"]}, message),
                error_message and html.div({"style": styles["error_message"]}, error_message),
            ),
            GroupsTable()
        )

    def SubjectForm():
        return html.div(
            {"style": styles["form"]},
            html.form(
                {"onSubmit": submit_subject},
                html.label({"style": styles["label"]}, "Название предмета"),
                html.input({
                    "type": "text",
                    "value": subject_name,
                    "onChange": lambda e: set_subject_name(e["target"]["value"]),
                    "required": True,
                    "style": styles["input"],
                }),
                html.button({
                    "type": "submit",
                    "disabled": loading,
                    "style": button_style(loading),
                }, "Добавить"),
                message and html.div({"style": styles["message"]}, message),
                error_message and html.div({"style": styles["error_message"]}, error_message),
            ),
            SubjectsTable()
        )

    form_map = {
        "teacher": TeacherForm,
        "group": GroupForm,
        "subject": SubjectForm,
        "schedule": lambda: ScheduleForm(
            styles=styles,
            groups=groups,
            teachers=teachers,
            subjects=subjects,
            schedule=schedule,
            loading=loading,
            set_message=set_message,
            set_error_message=set_error_message,
            set_loading=set_loading,
            load_all_data=load_data,
        ),
    }

    return html.div(
        {"style": styles["body"]},
        html.div(
            {"style": styles["sidebar"]},
            html.a(
                {
                    "href": logout_url,
                    "style": {
                        "color": "#e74c3c",
                        "fontWeight": "700",
                        "textDecoration": "none",
                        "marginBottom": "1rem",
                        "display": "inline-block",
                    },
                },
                "Выйти"
            ),
            html.button({"style": sidebar_button_style("teacher"), "onClick": lambda e: set_active_form("teacher")},
                        "Преподаватели"),
            html.button({"style": sidebar_button_style("group"), "onClick": lambda e: set_active_form("group")},
                        "Группы"),
            html.button({"style": sidebar_button_style("subject"), "onClick": lambda e: set_active_form("subject")},
                        "Предметы"),
            html.button({"style": sidebar_button_style("schedule"), "onClick": lambda e: set_active_form("schedule")},
                        "Расписание"),
        ),
        html.div(
            {"style": styles["content"]},
            form_map[active_form]()
        )
    )
